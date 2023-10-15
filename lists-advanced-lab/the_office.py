'''
You will receive two lines of input:
    • a list of employees' happiness as a string of numbers separated by a single space
    • a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
    • If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
    • Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
'''


def check_happiness(lh: list) -> int:
    count_of_employees = len(lh)
    sum_of_employees = 0
    filter_count = 0
    for s in range(count_of_employees):
        sum_of_employees += lh[s]
    for happiness in range(count_of_employees):
        if lh[happiness] >= sum_of_employees / count_of_employees:
            filter_count +=1
    return filter_count


list_of_employees = input().split()
lenght_of_employees= len(list_of_employees)
happiness_improvement_factor = int(input())
level_happiness = [(int(happiness) * happiness_improvement_factor) for happiness in list_of_employees ]
result = check_happiness(level_happiness)
if result >= (lenght_of_employees / 2):
    print(f'Score: {result}/{lenght_of_employees}. Employees are happy!')
else:
    print(f'Score: {result}/{lenght_of_employees}. Employees are not happy!')