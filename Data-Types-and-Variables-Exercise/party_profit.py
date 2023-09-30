group_member = int(input())
days = int(input())
every_day = 0
profit_per_day = 0
result = 0
for day in range (1, days + 1):
    if day % 5 == 0:
        if day % 15 == 0:
            group_member += 5
        if day % 10 == 0:
            group_member -= 2
        profit_per_day += (group_member * 20)
        if day % 15 == 0:
            profit_per_day -= (group_member * 5)
    elif day % 3 == 0:
        profit_per_day -= (group_member * 3)
    every_day = 50 - (group_member * 2)
    profit_per_day += every_day

result = int(profit_per_day / group_member)
print(f'{group_member} companions received {result} coins each.')
