n = int(input())
for i in range(1, n+1):
    sum = 0
    n_str = str(i)
    for string in n_str:
        sum += int(string)
    is_special = False
    if sum == 5 or sum == 7 or sum == 11:
        is_special = True
    print(f'{i} -> {is_special}')