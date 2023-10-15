'''
Which Are In?
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line.
'''


def search_word_in_strings(main_string_one:list, main_string_two: list) -> list:
    result = []
    for str_one in main_string_one:
        for str_two in main_string_two:
            if str_one in str_two:
                result.append(str_one)
                break
    return result


string_one = input().split(', ')
string_two = input().split(', ')
result_from_def_search_word_in_strings = search_word_in_strings(string_one, string_two)
print(result_from_def_search_word_in_strings)