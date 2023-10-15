'''
Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
'''

def factorials(n: int) -> int:
    fac_number = 1
    for i in range(1,n+1):
        fac_number *= i
    return fac_number

result = []
for _ in range(2):
    number = int(input())
    factorials(number)
    result.append(factorials(number))
total_result = (result[0] / result[1])
print(f'{total_result:.2f}' )