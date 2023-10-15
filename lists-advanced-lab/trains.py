'''
You will receive a number representing the number of wagons a train has.
Create a list (train) with the given length containing only zeros.
Until you receive the command "End", you will receive some of the following commands:

· "add {people}" – you should add the number of people in the last wagon

· "insert {index} {people}" - you should add the number of people at the given wagon

· "leave {index} {people}" - you should remove the number of people from the wagon.
There will be no case in which the people will be more than the count in the wagon.

There will be no case in which the index is invalid!

After you receive the "End" command print the train.
'''

wagon_number = int(input())
train = [0 for _ in range(wagon_number)]
command_list = ['End', 'add', 'insert', 'leave']
while True:
    command = input().split()
    if command[0] == command_list[0]:
        break
    if command[0] == command_list[1]:
        number_of_people = (int(command[1]))
        train[-1] += number_of_people
    elif command[0] == command_list[2]:
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == command_list[3]:
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
print(train)