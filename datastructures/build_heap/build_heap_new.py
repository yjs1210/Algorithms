# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    def left_child(idx):
        return idx*2 + 1
    
    def right_child(idx):
        return idx*2 + 2 

    def sift_down(arr, idx, size, swaps):
        maxIndex = idx
        l = left_child(idx) 
        if (l <= (size-1)):
            if (arr[l] < arr[maxIndex]):
                maxIndex = l
        r = right_child(idx)
        if (r <= (size-1)):
            if (arr[r] < arr[maxIndex]):
                maxIndex = r
        if idx != maxIndex:
            swaps.append((idx, maxIndex))
            temp = arr[idx]
            arr[idx] = arr[maxIndex]
            arr[maxIndex] = temp
            sift_down(arr, maxIndex, size, swaps)

    size = len(data)
    swaps = []
    for i in range(size//2 - 1, -1, -1):
        sift_down(data, i, size, swaps)

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
