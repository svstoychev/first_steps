def check_palindrome(n: list)  -> list:
    reversed_list = []
    for i in n:
        reversed_list.append(i[::-1])
    for l in range(len(n)):
        if n[l] == reversed_list[l]:
            result_list.append(True)
        else:
            result_list.append(False)
    return  result_list

numbers = input().split(', ')
result_list = []
check_palindrome(numbers)
for result in result_list:
    print(result)