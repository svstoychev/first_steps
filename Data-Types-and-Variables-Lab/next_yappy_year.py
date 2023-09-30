#You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
year = int(input())
number_of_year = []
while True:
    year += 1
    if (len(str(year))) == (len(set(str(year)))):
        break
print(year)