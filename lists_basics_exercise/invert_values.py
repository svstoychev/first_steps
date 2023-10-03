#Write a program that receives a single string containing positive and negative numbers separated by a single space.
#Print a list containing the opposite of each number.

number = input().split()
for i in range (len(number)):
    if int(number[i]) >= 0:
        number[i] = (int(number[i])*(-1))
    else:
        number[i] = (int(number[i])*(-1))
print(number)