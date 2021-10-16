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

# Returns max subarray within a[i:j] (inclusive of i, exclusive of j)
def impl(a, i, j):
    #print(i, j)
    if j - i <= 0:
        return []
    if j - i == 1:
        return a[i:j]

    # ignore non-positive elements at the edges WRONG: [1, -999999, 2]
    # need to check how far we can spread from the center instead
    while i < j - 1 and a[i] <= 0:
        i += 1
    while i < j - 1 and a[j - 1] <= 0:
        j -= 1
    #print(a, i, j)
    bestUnbroken = total(a[i:j])

    # break in half
    mid = int((i + j) / 2)    
    left = impl(a, i, mid)
    right = impl(a, mid, j)
    leftTotal = total(left)
    rightTotal = total(right)

    # return either a half, or the total, whichever is max
    if (max(leftTotal, rightTotal, bestUnbroken) == bestUnbroken):
        return a[i:j]
    elif (max(leftTotal, rightTotal, bestUnbroken) == rightTotal):
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
