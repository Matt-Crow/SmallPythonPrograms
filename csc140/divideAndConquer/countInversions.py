"""
Given an array of numbers, count how many numbers come before a number less than
it.

Ex.
    countInversions([1, 2, 3]) = 0
    countInversions([3, 2, 1]) = 2
    countInversions([2, 1, 3]) = 1

not sure if this works
"""



import random



def test():
    a = createArray(10)
    i = countInversions(a)
    print(f'{a} contains {i} inversions')
    d = [e for e in a]
    impl(d, 0, len(d))
    print(f'Sorted: {d}')

def createArray(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, 100))
    return a

def countInversions(a):
    #            copy of a
    return impl([e for e in a], 0, len(a))

def impl(a, start, end):
    if end - start <= 1:
        return 0 # all elements in order
    # sort a for the caller, return number of swaps needed to get there

    swaps = 0
    mid = int((start + end) / 2)
    swaps += impl(a, start, mid)
    swaps += impl(a, mid, end)
    # swaps contains total number of swaps needed to get each half in order
    # a[start:mid] and a[mid:end] are both in order

    newA = []
    i = start
    j = mid

    while i < mid and j < end:
        if a[i] <= a[j]:
            newA.append(a[i])
            i += 1
        else:
            newA.append(a[j])
            j += 1
            swaps += (mid - i)
            """
            From lecture:
            a[j] is smaller than the smallest element in a[i:mid]
            since a[start:mid] is sorted, a[i] is the smallest in that range
            therefore, each element in a[i:mid] are larger than a[j], yet to its
            left, so (mid - i) inversions
            """
    while i < mid:
        newA.append(a[i])
        i += 1
    while j < end:
        newA.append(a[j])
        j += 1

    for n in range(len(newA)):
        a[start + n] = newA[n]

    return swaps



if __name__ == "__main__":
    test()
