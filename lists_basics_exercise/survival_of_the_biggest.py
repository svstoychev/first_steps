# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers
# that are left in the list, separated by a comma and a space ", ".

numbers = input().split()
numbers_int = []
count_of_number_to_remove_from_the_list = int(input())
for i in range(len(numbers)):
    numbers_int.append(int(numbers[i]))
for number in range (count_of_number_to_remove_from_the_list):
    min_number = min(numbers_int)
    numbers_int.remove(min_number)
count = 1
new_string = []
for j in range (len(numbers_int)):
    if count < len(numbers_int):
        strings = str(numbers_int[j]) + ', '
        new_string.append(strings)
        count += 1
    else:
        new_string.append(str(numbers_int[-1]))
for k in new_string:
    print(k, end='')