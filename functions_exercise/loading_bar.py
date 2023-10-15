'''
You will receive a single integer number between 0 and 100 (inclusive)
divisible by 10 without remainder (0, 10, 20, 30...).
Your task is to create a function that returns a loading bar depending on the number you have received in the input.
Print the result on the console. For more clarification, see the examples below.
'''

def loading_bar(n: int) ->str:
    percent = 0
    if n == 100:
        return (f'100% Complete! \n[%%%%%%%%%%]')
    elif n % 10 == 0:
        percent = n // 10
        point_persent = 10 - percent
        return (str(n) + "% " + ("[" + "%" * percent + "." * point_persent + "]\nStill loading..."))


number = int(input())
print(loading_bar(number))