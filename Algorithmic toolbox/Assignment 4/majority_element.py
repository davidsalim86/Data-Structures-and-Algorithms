def majority_element(elements):
    candidate = None
    count = 0

    for e in elements:
        if count == 0:
            candidate = e
            count = 1
        elif candidate == e:
            count += 1
        else:
            count -= 1

    # At this point, `candidate` contains a potential majority element,
    # but we need to verify if it actually occurs more than n/2 times.
    count = elements.count(candidate)
    if count > len(elements) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))