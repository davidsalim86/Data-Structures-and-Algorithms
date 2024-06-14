def binary_search(keys, array):
    # write your code here

    low, high =0, len(array)-1
    
    while low <= high:
        mid = low + (high - low)//2    
        if array[mid] == keys:
            return mid
        elif array[mid] < keys:
            low = mid + 1
        else:
            high = mid -1
    return -1
    

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(q, input_keys), end=' ')

