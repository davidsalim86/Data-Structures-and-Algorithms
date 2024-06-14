def compute_operations(n):
    min_operations = [0] * (n + 1)
    operations_sequence = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        min_operations[i] = min_operations[i - 1] + 1
        operations_sequence[i] = operations_sequence[i - 1] + [i]

        if i % 2 == 0 and min_operations[i // 2] + 1 < min_operations[i]:
            min_operations[i] = min_operations[i // 2] + 1
            operations_sequence[i] = operations_sequence[i // 2] + [i]

        if i % 3 == 0 and min_operations[i // 3] + 1 < min_operations[i]:
            min_operations[i] = min_operations[i // 3] + 1
            operations_sequence[i] = operations_sequence[i // 3] + [i]

    return operations_sequence[n]

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)