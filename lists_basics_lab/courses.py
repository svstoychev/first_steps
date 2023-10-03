#On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses. You should create a list of courses and print it.
number_n = int(input())
name = []
for i in range(number_n):
    names = input().strip()
    name.append(names)
print(name)