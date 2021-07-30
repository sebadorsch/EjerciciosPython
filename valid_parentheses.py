def valid_parentheses(string):
    cont = 0
    for i in string:
        if i == "(": cont += 1
        elif i == ")": cont -= 1
        if cont < 0: return False
    return True if cont == 0 else True

"""
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""



if __name__ == '__main__':
    """
    print(valid_parentheses("  ("), False)
    print(valid_parentheses(")test"), False)
    print(valid_parentheses(""), True)
    print(valid_parentheses("hi())("), False)
    """
    print(valid_parentheses("hi(hi)()"), True)