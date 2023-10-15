def min_max_sum(number: list) -> list:
    numbers = []
    numbers.append(min(number))
    numbers.append(max(number))
    numbers.append(sum(number))
    return numbers

numbers = input().split(' ')
numbers_int = []
for n in numbers:
    numbers_int.append(int(n))
result_list = []
result_list = min_max_sum(numbers_int)
print(f'The minimum number is {result_list[0]}')
print(f'The maximum number is {result_list[1]}')
print(f'The sum number is: {result_list[2]}')