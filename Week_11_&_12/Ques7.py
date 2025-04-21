import sys

def matrix_chain_order(p):
    n = len(p) - 1 
    m = [[0 for _ in range(n)] for _ in range(n)]  

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]

p = [10, 20, 30, 40, 30]
min_cost = matrix_chain_order(p)

print("Minimum number of multiplications is:", min_cost)
