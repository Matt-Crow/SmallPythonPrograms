


def bin2dec(binStr):
    return impl(binStr, 1)

def impl(binStr, twoExp):
    sum = 0
    if len(binStr) > 0:
        term = 0
        if binStr[len(binStr) - 1] == '1':
            term = twoExp
        sum = term + impl(binStr[:(len(binStr) - 1)], twoExp * 2)
    return sum

if __name__ == "__main__":
    print(bin2dec("1111"))
    print(bin2dec("1010"))
    print(bin2dec("11111111"))
