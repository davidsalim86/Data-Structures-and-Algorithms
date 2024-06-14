def largest_number(numbers):
    numbers = list(map(str, numbers))
    compare = lambda x: x*3
    sort = "".join(sorted(numbers,key=compare, reverse=True))
    return sort


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(largest_number(input_numbers))
