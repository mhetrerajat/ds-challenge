# https://www.geeksforgeeks.org/find-expression-duplicate-parenthesis-not/


def check(n):
    stack = []
    is_last_poped_parenthesis = False
    for i in n:
        print(n, stack, i, is_last_poped_parenthesis)
        if i == ")":
            _i = stack.pop()
            if is_last_poped_parenthesis and _i == "(":
                return True

            while _i != "(":
                _i = stack.pop()

                if _i == "(":
                    is_last_poped_parenthesis = True
        else:
            is_last_poped_parenthesis = False
            stack.append(i)

    return False


def main():
    N = [
        "((a+b)+((c+d)))",
        "(((a+(b))+c+d))",
        "(((a+(b)))+(c+d))",
        "((a+b)+(c+d)) ",
        "((a+(b))+(c+d))"
    ]
    for n in N:
        print(check(n))


if __name__ == "__main__":
    main()
