import re, netmiko, paramiko
from ping3 import ping, verbose_ping

def system_identity() ->str:
    stdin, stdout, stderr = ssh.exec_command(f'/system/identity/print')
    devicename = stdout.read().decode().strip()
    return devicename[6:]


def clocktime() ->str:
    stdin, stdout, stderr = ssh.exec_command(f'system/clock/print')
    c = stdout.read().decode().strip(' ')
    times = ''
    for i in range(len(c)):
        if c[i] != ' ' and c[i] != '\n' and c[i] != '\r':
            clock.append(c[i])
    for l in range(5, 13):
        times += clock[l]
    return times

def dates():
    stdin, stdout, stderr = ssh.exec_command(f':put [/system/clock/get date];')
    date = stdout.read().decode()
    year = date[:4]
    mount = date[4:8]
    day = date[8:10]
    date = day+mount+year
    return date.rstrip()

def boardname() ->str:
    stdin, stdout, stderr = ssh.exec_command(f':put [/system/routerboard/get board-name ];')
    board = stdout.read().decode()
    return board.rstrip()

def version() -> str:
    stdin, stdout, stderr = ssh.exec_command(f':put [system/resource/get version];')
    versions = stdout.read().decode()
    return versions.rstrip()

def backups(back) -> str:
    stdin, stdout, stderr = ssh.exec_command(f'/export file="{back}";')
    stdin, stdout, stderr = ssh.exec_command(f'/system/backup/save name="{back}";')
    bac = stdout.read().decode()
    return bac.rstrip()


mikrotik_address = {'core':'10.3.0.1','wireless':'10.3.0.2' }
username = 'networkeng'
password = "0radiet0n3tw0rk3ng"
port = 6969
no_connection = {}
not_conn_count = 0
clock = []
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for key, value in mikrotik_address.items():
    responce = ping(mikrotik_address[key], timeout=2)
    if responce is None:
        no_connection[key] = value
        not_conn_count += 1
        continue
    ssh.connect(mikrotik_address[key],port=port,username=username, password=password)
    device_name = system_identity();
    clock_time = clocktime()
    backup = device_name + '-' + boardname() + '-'+ 'v.' +version() + '-' + dates() + '-' + clock_time
    print(f'{mikrotik_address[key]} - {backups(backup)}')
    print('##################')
ssh.close()
if not_conn_count > 0:
    print(f'No connection to {no_connection}')
else:
    print(f'All backups has been saved successful')