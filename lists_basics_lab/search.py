#On the first line, you will receive a number n.
# On the second line, you will receive a word. On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

n = int(input())
word = input()
save_string = []
filtered_string = []
for i in range(n):
    input_the_string = input()
    save_string.append(input_the_string)
print(save_string)
for j in range(n):
    if word in save_string[j]:
        filtered_string.append(save_string[j])
print(filtered_string)