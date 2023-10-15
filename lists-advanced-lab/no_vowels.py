'''
Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
Print the new text string after removing the vowels.
The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
'''

def results(inp_str: str, letter: list) ->list:
    result = [result_strings for result_strings in inp_str if result_strings.lower() not in letter]
    return result


letter_need_remove_form_list = ['a', 'o', 'u', 'e', 'i']
input_string = input()
result_string = results(input_string, letter_need_remove_form_list)
print(''.join(result_string))   