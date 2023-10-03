#On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
#    • even
#    • odd
#    • negative
#    • positive
#Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

number = int(input())
list_number = []
new_list = []
for i in range(number):
    command = int(input())
    list_number.append(command)
command = input()
for j in range(len(list_number)):
    numbers = int(list_number[j])
    if command == 'even':
        if numbers % 2 == 0:
            new_list.append(numbers)
    elif command == 'odd':
        if numbers % 2 != 0:
            new_list.append(numbers)
    elif command == 'negative':
        if numbers < 0:
            new_list.append(numbers)
    elif command == 'positive':
        if numbers >= 0 :
            new_list.append(numbers)
print(new_list)