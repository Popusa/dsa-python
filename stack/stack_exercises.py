import stack as s

arr = s.stack()

# 1. Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"


def reverse_string(str):
    [arr.push(letter) for letter in str]
    reversed_string = ""
    reversed_string = [reversed_string + arr.pop() for letter in str]
    return ''.join(reversed_string)

# 2. Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

def is_match(char1,char2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[char1] == char2


def is_balanced(str):
    # NO STACK 

    # open_par = 0
    # closed_par = 0
    # open_square = 0
    # closed_square = 0
    # open_curly = 0
    # closed_curly = 0
    # for i in range(len(str)):
    #     if str[0] == ')' or str[0] == "}" or str[0] == "]":
    #         return False
    #     elif str[i] == '(':
    #         open_par += 1
    #     elif str[i] == ')':
    #         closed_par += 1
    #     elif str[i] == '[':
    #         open_square += 1
    #     elif str[i] == ']':
    #         closed_square += 1
    #     elif str[i] == '{':
    #         open_curly += 1
    #     elif str[i] == '}':            
    #         closed_curly += 1
        
    # if open_par != closed_par or open_square != closed_square or open_curly != closed_curly:
    #     return False
    # else:
    #     return True

    #STACK
    stack = s.stack()
    for char in str:
        if char=='(' or char=='{' or char == '[':
            stack.push(char)
        if char==')' or char=='}' or char == ']':
            if stack.size()==0:
                return False
            if not is_match(char,stack.pop()):
                return False

    return stack.size()==0

print(reverse_string("We will conquere COVID-19"))

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))