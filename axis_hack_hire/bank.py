from collections import Counter


def generate_adj_matrix(v, e):
    n = len(v) # Number of vertex
    matrix = [[0]*n for _ in range(n)]

    for idxi, i in enumerate(v):
        for idxj, j in enumerate(v):
            if i != j:
                if (i,j) in e or (j, i) in e:
                    matrix[idxi][idxj] = 1
                    matrix[idxi][idxj] = 1

    
    return matrix

def find_degree(vertexes, idx, matrix, dgr_cache):
    if idx in dgr_cache:
        return dgr_cache[idx]

    d = 0
    n = len(vertexes)
    for i in range(n):
        if matrix[idx][i] == 1:
            d += 1
    dgr_cache.update({ idx : d })

    return d

def validate_bank(vertexes, edges):
    matrix = generate_adj_matrix(vertexes, edges)
    
    # both vertex degree 1, then -1 -1
    # i vertex degree 1 and j vertex degree greater than 1 then 1, 0
    # i vertex degree greater than 1 and j vertex degree 1 then 0, 1
    # both vertex degree greater than 1 then -1, -1

    degrees = {}
    for (i,j) in edges:
        idxi = vertexes.index(i)
        idxj = vertexes.index(j)

        di = find_degree(vertexes, idxi, matrix, degrees)
        dj = find_degree(vertexes, idxj, matrix, degrees)

        if di == 1 and dj == 1:
            print(-1, -1)
        elif di == 1 and dj > 1:
            print(1, 0)
        elif di > 1 and dj == 1:
            print(0, 1)
        else:
            print(-1, -1)



def main():
    vertexes = set()
    edges = []
    while True:
        a, b = map(int, input().strip().split())
        if a == -1 and b == -1:
            break
        else:
            vertexes.update([a,b])
            
            item = (a,b)
            if item not in edges:
                edges.append(item)
    
    # To keep ordering
    vertexes = list(vertexes)
    validate_bank(vertexes, edges)

if __name__ == "__main__":
    main()
