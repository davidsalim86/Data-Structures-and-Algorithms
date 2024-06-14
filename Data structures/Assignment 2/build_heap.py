# python3

def build_heap(data):
    swaps = []
    def sift_down(i):
        nonlocal swaps
        max_Index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(data) and data [left_child] < data[max_Index]:
            max_Index = left_child
        
        if right_child < len(data) and data[right_child] < data[max_Index]:
            max_Index = right_child
            
        if i != max_Index:
            swaps.append((i, max_Index))
            data[i], data[max_Index] = data[max_Index], data[i]
            sift_down(max_Index)
            
    for i in range (len(data)//2,-1,-1):
        sift_down(i)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
