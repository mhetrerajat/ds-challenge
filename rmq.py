import math
import sys

# Trivial solution
def trivial(A, length):
    matrix = [[0]*length for _ in range(length)] 
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

def trivial_rmq(A, length, n1, n2):
    # Preprocessing matrix
    matrix = trivial(A, length)
    return matrix[n1][n2]



# sqrt solution
def batch_process(A, length):
    batch_size = math.floor(math.sqrt(length))
    m_size = math.ceil(length/batch_size) 
    M = [0] * m_size
    
    min_element = sys.maxsize
    min_element_idx = 0
    for idx, item in enumerate(A):
        if min_element > item:
            min_element = item
            min_element_idx = idx

        if (idx+1) % batch_size == 0:
            _idx = ((idx+1) // batch_size) - 1
            M[_idx] = min_element_idx
            min_element = sys.maxsize
            min_element_idx = 0
            
    return M, batch_size

def sqrt_rmq(A, length, n1, n2):
    M, batch_size = batch_process(A, length)

    min_element = n1
    # First block
    while n1%batch_size != 0 and n1 != 0 and n1 < n2:
        if A[min_element] > A[n1]:
            min_element = n1
        n1 += 1
   
    # Range
    while (n1 + batch_size) <= n2:
        if A[min_element] > A[M[n1//batch_size]]:
            min_element = M[n1//batch_size]
        n1 += batch_size


    # Last block
    while n1 <= n2:
        if A[min_element] > A[n1]:
            min_element = n1
        n1 += 1

    return min_element

def rmq(A, length, n1, n2):
    return sqrt_rmq(A, length, n1, n2)

if __name__ == "__main__":
    A = [2,4,3,1,6,7,8,9,1,7]
    length = len(A)
    
    # Find rmq
    n1, n2 = 2, 7
    rmq = rmq(A, length, n1, n2)
    assert rmq == 3 # index of min value
