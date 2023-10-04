#
number = int(input())
status = False
if number == 1:
    print(f'False')
elif number > 1:
    for i in range(2,number):
        if number % i == 0:
            status = True
            break
    if status:
        print(f'False')
    else:
        print(f'True')
