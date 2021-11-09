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

    longest subsequence is [x, longestSubsequence(A2, B2)] # professor does in reverse

recursive solution: doesn't work, as it only searches for exactly A in B
f(A, B):
    if B is empty:
        return []
    else if A[0] in B:
        i is where A[0] is in B
        return A[0] union f(A[1...], B[i...])
    else:
        return f(A[1...], B)
"""



def test():
    pass



if __name__ == "__main__":
    test()
