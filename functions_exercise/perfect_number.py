'''
A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following messages:
    • "We have a perfect number!" - if the number is perfect.
    • "It's not so perfect." - if the number is NOT perfect.
'''

def divisor_function(n: int) -> str:
    sum_divisor = 0
    for i in range(1,n):
        if n % i == 0:
            sum_divisor += i
    if n == sum_divisor:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


number = int(input())
print(divisor_function(number))

