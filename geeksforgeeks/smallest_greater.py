# https://practice.geeksforgeeks.org/problems/smallest-greater-elements-in-whole-array/0


def simple(N, A):
    for i in A:
        closest_idx = -1
        current_diff = 999999999 # Some large number
        for idx, j in enumerate(A):
            if abs(j - i) < current_diff and j > i:
                current_diff = j - i
                closest_idx = idx
        
        if closest_idx == -1:
            print("_", end=" ")
        else:
            print(A[closest_idx], end=" ")


    #print("Original : {0}".format(A))



def find_smallest_greater_element(N, A):
    simple(N, A)
    print("", end="\n")


def main():
    T = [
        (9, [6,3,9,8,10,2,1,15,7]),
        (4, [13,6,7,12])
    ]
    for (N, A) in T:
        find_smallest_greater_element(N, A)


if __name__ == "__main__":
    main()
