



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


def trivial_rmq(matrix, A, n1, n2):
    # Preprocessing matrix
    matrix = trivial(matrix, A, length)
    return matrix[n1][n2]

if __name__ == "__main__":
    A = [2,4,3,1,6,7,8,9,1,7]
    length = len(A)
    matrix = [[0]*length for _ in range(length)]
    
    # Find rmq
    n1, n2 = 2, 7
    rmq = trivial_rmq(matrix, A, n1, n2)
    assert rmq == 3 # index of min value
