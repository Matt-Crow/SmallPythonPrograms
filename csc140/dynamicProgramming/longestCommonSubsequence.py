"""
given 2 sequences, A and B, a common subsequence occurs when taking the element
i, j, ..., k for A in order, those same values occur in B in the same order
(note that there can be elements between them: ex. [1, 3] is a subsequence of [1, 4, 3])
Find longest subsequence.

A = [1, 2, 3, 4, 5]
B = [2, 6, 3, 7, 8, 9, 5]

Longest is [2, 3, 5]


Optimal Substructure:
    A = [...A1, x, ...A2]
    B = [...B1, x, ...B2]
    where x is the first match

    longest subsequence is [x, longestSubsequence(A2, B2)]
    professor does in reverse, checks only last element of each array each call

recursive solution:
f(A, B):
    if A or B is empty:
        return []
    else if A[0] == B[0]:
        return A[0] union f(A[1...], B[1...])
    else:
        return best solution between f(A[1...], B) and f(A, B[1...])

f(n, m) relies on f(n - 1, m - 1), f(n - 1, m), and f(n, m - 1)
[
    [x, x],
    [x, o]
]
x's must be solved before o
"""



def test():
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 6, 3, 7, 8, 9, 5]
    solution = longestSubsequence(list1, list2)
    print(solution)

def longestSubsequence(list1, list2):
    """
    NxM array len list1 by len list2
    matches[i][j] shows num matches between first i+1 elements of list1 and
    first j+1 elements of list2

    Initialize by locating where the first matches between first elements occur
    """
    matches = []
    for i in range(0, len(list1)):
        matches.append([])
        for j in range(0, len(list2)):
            matches[i].append(0)
        if list1[i] == list2[0]:
            matches[i][0] += 1
    for j in range(0, len(list2)):
        if list1[0] == list2[j]:
            matches[0][j] += 1

    """
    solve in a series of check-mark shapes
    1 1 1 1
    1 2 2 2
    1 2 3 3
    1 2 3 4
    1 2 3 4
    in this order

    could just use a standard
    for i in range(1, len(list1)):
        for j in range(1, len(list2)):
            ...
    since that order still means each solution has access to its subsolutions
    """
    for offset in range(1, min(len(list1), len(list2))):
        for i in range(offset, len(list1)): # Theta(N)
            matches[i][offset] = max(
                matches[i - 1][offset - 1],
                matches[i - 1][offset],
                matches[i][offset - 1]
            )
            if list1[i] == list2[offset]:
                matches[i][offset] += 1
        #              matches[offset][offset] has already been computed
        for j in range(offset + 1, len(list2)): # Theta(M)
            matches[offset][j] = max(
                matches[offset - 1][j - 1],
                matches[offset - 1][j],
                matches[offset][j - 1]
            )
            if list1[offset] == list2[j]:
                matches[offset][j] += 1

    for line in matches:
        print(line)

    return matches[len(list1) - 1][len(list2) - 1]


if __name__ == "__main__":
    test()
