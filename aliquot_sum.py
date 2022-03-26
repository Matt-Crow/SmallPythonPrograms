"""
An aliquot sum s(n) of a number n is the sum of all factors of the number except
for the number itself.

For example, given n = 20, s(n) = 1 + 2 + 4 + 5 + 10 = 22
"""

from functools import reduce

EXPECTED = [
    0, 1, 1, 3, 1, 6, 1, 7, 4, 8,
    1, 16, 1, 10, 9, 15, 1, 21, 1, 22,
    11, 14, 1, 36, 6, 16, 13, 28, 1, 42,
    1, 31, 15, 20, 13, 55, 1, 22, 17, 50,
    1, 54, 1, 40, 33, 26, 1, 76, 8, 43,
    21, 46, 1, 66, 17, 64, 23, 32, 1, 108,
    1, 34, 41, 63, 19, 78, 1, 58, 27, 74,
    1, 123, 1, 40, 49, 64, 19, 90, 1, 106
]


"""
function prototype defines a contract between this function and those who use it
"if you give me a whole number, I'll give you a whole number back"
It is expected that 0 < n and this will give back something non-negative
"""
def aliquotSum(n: int)->int:
    sum = 0                  # initilize sum to 0
    i = n - 1                # s(n) is defined as excluding n
    while i > 0:             # repeat these 3 lines until i is 0 or less
        if n % i == 0:       # "is i a factor of n?" <=> n / i has no remainder
            sum += i         # sum = sum + i
        i -= 1               # decrease to get the next number to check
    return sum               # "give back" the sum to the caller

def functionalAliquotSum(n: int)->int:
    return reduce(                              # squashes list into one value
        lambda x, y: x + y,                     # add sum thus far to current element
        (i for i in range(1, n) if n % i == 0), # "each i from 1 to n that is a factor of n"
        0                                       # start at sum of 0
    )

if __name__ == "__main__":
    ss = []
    sn = None
    for n in range(1, 60):
        sn = aliquotSum(n) # or functionalAliquotSum(n)
        print(f's({n}) = {sn}') # notice how prime numbers s(n) is 1
        ss.append(sn)


    for i in range(min(len(ss), len(EXPECTED))):
        if ss[i] != EXPECTED[i]:
            raise Exception(f'fail s({i})')
    print("all tests passed successfully")
