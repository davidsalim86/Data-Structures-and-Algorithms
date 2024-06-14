def fibonacci_number(n):
    f=[0,1]
    for i in range(2, n+1):
        f.append(f[i - 1] + f[i - 2])
    return f [n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
