# Shunting yard algorithm
# RPM : infix -> postfix

def rpm(s):
    stack = []
    result = []
    is_operand = lambda x : x.isdigit()
    is_operator = lambda x : x in ["+", "-", "*", "/", "^"]
    is_left_bkt = lambda x : x == "("
    is_right_bkt = lambda x : x == ")"
    precedence = { '+': 1, '-': 1, '*':2, '/': 2 , "^": 3}
    associative = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', "^": "right"}

    for x in s:
        if " " == x:
            continue
        elif is_operand(x):
            result.append(x)
        elif is_operator(x):
            top = stack[-1] if stack else None
            top_precedence = precedence.get(top, 0) if top else 0
            x_precedence = precedence.get(x, 0)
            x_associative = associative.get(x)
            op_cnd = any([top_precedence > x_precedence, (top_precedence == x_precedence) and top_precedence != 0 and x_precedence != 0 and x_associative == "left" ])

            while(op_cnd and top != "("):
                _i = stack.pop()
                result.append(_i)
                top = stack[-1] if stack else None
                top_precedence = precedence.get(top, 0) if top else 0
                op_cnd = any([top_precedence > x_precedence, (top_precedence == x_precedence) and top_precedence != 0 and x_precedence != 0 and x_associative == "left" ])

            stack.append(x)
        elif x == "(":
            stack.append(x)
        elif x == ")":
            top = stack[-1] if stack else None
            while(top != "(" and top is not None):
                _i = stack.pop()
                top = stack[-1] if stack else None
                result.append(_i)
            stack.pop() # pop left bracket

    stack.reverse()
    result.extend(stack)
    return "".join(result)




def main():
    T = [
       "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3",
       "4 + 3 * π "
    ]
    for t in T:
        print(rpm(t))



if __name__ == "__main__":
    main()
