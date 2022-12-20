# https://www.geeksforgeeks.org/generate-lexicographically-smallest-string-of-0-1-and-2-with-adjacent-swaps-allowed/


def get_answer(t):
    ones = t.count('1')
    result = []

    is_all_ones_used = False
    for i in t:
        if i == "2" and not is_all_ones_used:
            for _ in range(ones):
                result.append("1")
            is_all_ones_used = True

        if i != "1":
            result.append(i)


    if not is_all_ones_used:
        for _ in range(ones):
            result.append("1")
        

    return "".join(result)

def main():
    T = ["100210", "2021"]
    for t in T:
        print("q : {0}".format(t))
        t = list(t)
        print("".join(get_answer(t)))


if __name__ == "__main__":
    main()
