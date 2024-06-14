from random import randint


def partition3(array, left, right):
    pivot = array[left]
    less_than_pivot = left
    equal_to_pivot = left
    for i in range(left + 1, right + 1):
        if array[i] < pivot:
            less_than_pivot += 1
            equal_to_pivot += 1
            array[i], array[less_than_pivot] = array[less_than_pivot], array[i]
            if equal_to_pivot != less_than_pivot:
                array[i], array[equal_to_pivot] = array[equal_to_pivot], array[i]
        elif array[i] == pivot:
            equal_to_pivot += 1
            array[i], array[equal_to_pivot] = array[equal_to_pivot], array[i]
    array[left], array[less_than_pivot] = array[less_than_pivot], array[left]
    return less_than_pivot, equal_to_pivot


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)