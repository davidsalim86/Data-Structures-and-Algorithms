def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def maximum_value(dataset):
    n = (len(dataset) + 1) // 2
    min_matrix = [[0] * n for _ in range(n)]
    max_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        min_matrix[i][i] = int(dataset[2*i])
        max_matrix[i][i] = int(dataset[2*i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val = float('inf')
            max_val = float('-inf')
            for k in range(i, j):
                op = dataset[2 * k + 1]
                a = evaluate(max_matrix[i][k], max_matrix[k+1][j], op)
                b = evaluate(max_matrix[i][k], min_matrix[k+1][j], op)
                c = evaluate(min_matrix[i][k], max_matrix[k+1][j], op)
                d = evaluate(min_matrix[i][k], min_matrix[k+1][j], op)
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_matrix[i][j] = min_val
            max_matrix[i][j] = max_val

    return max_matrix[0][n-1]

if __name__ == "__main__":
    print(maximum_value(input()))