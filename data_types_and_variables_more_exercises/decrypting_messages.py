#
key = int(input())
number_of_lines = int(input())
decrypt = []
result = 0
for i in range (number_of_lines):
    letter = input()
    result = key + int(ord(str(letter)))
    decrypt.append(chr(result))
for word in decrypt:
    print(f'{word}', end='')