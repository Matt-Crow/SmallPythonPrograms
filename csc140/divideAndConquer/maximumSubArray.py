"""
Given an array of numbers, find the subarray that maximizes the sum of all
elements in the array. Note that these numbers can be negative
"""



import random



def createArray(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(-10, 10))
    return nums

def bruteForceBest(a):
    best = a
    bestTotal = total(a)
    for end in range(len(a)):
        for start in range(end + 1):
            t = total(a[start:(end + 1)])
            if bestTotal < t:
                bestTotal = t
                best = a[start:(end + 1)]
    return best

def total(a):
    sum = 0
    for n in a:
        sum = sum + n
    return sum

def maxSubArray(a):
    return impl(a, 0, len(a))

# Returns max subarray within a[min:max] (inclusive of min, exclusive of max)
def impl(a, min, max):
    #print(min, max)
    if max - min <= 0:
        return []
    if max - min == 1:
        return a[min:max]

    # ignore non-positive elements at the edges
    while min < max - 2 and a[min] <= 0:
        min += 1
    while min < max - 2 and a[max - 1] <= 0:
        max -= 1
    bestUnbroken = total(a[min:max])

    # break in half
    mid = int((min + max) / 2)
    left = impl(a, min, mid)
    right = impl(a, mid, max)
    leftTotal = total(left)
    rightTotal = total(right)

    # return either a half, or the total, whichever is max
    if (leftTotal <= rightTotal and rightTotal <= bestUnbroken) or (rightTotal <= leftTotal and leftTotal <= bestUnbroken):
        return a[min:max]
    elif (leftTotal <= bestUnbroken and bestUnbroken <= rightTotal) or (bestUnbroken <= leftTotal and leftTotal <= rightTotal):
        return right
    else:
        return left

if __name__ == "__main__":
    a = createArray(100)
    print(a)
    bruteForce = bruteForceBest(a)
    print(f'Brute force found {bruteForce} {total(bruteForce)}')
    best = maxSubArray(a)
    print(f'Best: {best} {total(best)}')
