'''
Even Numbers
Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers.
'''

def even_number(n: list) -> list:
    even_numbers =  ([index for index, numbers_even in enumerate(n) if (int(numbers_even) % 2 == 0)])
    return even_numbers


number = input().split(', ')
result = even_number(number)
print(f'{result}')