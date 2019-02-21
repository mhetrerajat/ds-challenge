



def trivial(matrix, A, length):
    for i in range(length):
        matrix[i][i] = i

    for i in range(length):
        for j in range(i+1, length):
            # Compare with just previous range of elements
            if A[matrix[i][j-1]] >= A[j]:
                matrix[i][j] = j
            else:
                matrix[i][j] = matrix[i][j-1]


    return matrix


def process(matrix, A, length):
    return trivial(matrix, A, length)


if __name__ == "__main__":
    A = [2,4,3,1,6,7,8,9,1,7]
    length = len(A)
    matrix = [[0]*length for _ in range(length)]
    matrix = process(matrix, A, length)
    print(matrix)
