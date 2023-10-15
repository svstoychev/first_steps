'''
Palindrome Strings
On the first line, you will receive words separated by a single space.
On the second line, you will receive a palindrome.
First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".
'''

def reverse_word(word: list) -> list:
    for w in word:
        reversed_word = ''.join(reversed(w))
        if w == reversed_word:
            all_words.append(w)
    return all_words

def palindrom_count (p: str, aw: list) -> int:
    count = 0
    for i in range(len(aw)):
        if p == aw[i]:
            count += 1
    return count




words = input().split()
all_words = []
palindrom = input()

print(reverse_word(words))
print(f'Found palindrome {palindrom_count(palindrom, words)} times')
