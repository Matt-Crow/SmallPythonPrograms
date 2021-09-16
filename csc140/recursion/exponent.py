"""
returns base^exp



Proof by mathematical induction:

Base Case: base = b, exp = 0
    pow(b, 0) = 1 True

Inductive Step: (pow(b, e) = b^e) --> pow(b, e + 1) = b^(e+1)
    pow(b, e + 1) = b * pow(b, e + 1 - 1) = b * pow(b, e)
    apply the inductive hypothesis
    pow(b, e + 1) = b * b^e = b^(e+1)
    [#]
"""
def pow(base, exp, call = 1):
    print(f'regular call {call}')
    result = 1
    if exp > 0:
        result = base * pow(base, exp - 1, call + 1)
    return result


def powOptimized(base, exp, call = 1):
    print(f'optimized call {call}')
    result = 1
    if exp == 0:
        result = 1
    elif exp % 2 == 0:
        """
        b^2k = (b^2)^k
        """
        newExp = int(exp / 2)
        newBase = base * base
        result = powOptimized(newBase, newExp, call + 1)
    else:
        result = base * powOptimized(base, exp - 1, call + 1)
    return result

if __name__ == "__main__":
    print(pow(2, 32))
    print(powOptimized(2, 32))
