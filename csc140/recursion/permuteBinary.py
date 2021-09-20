


def permuteBinary(digits):
    for bin in impl(digits):
        print(bin)

def impl(digits):
    strs = []
    if digits <= 0:
        strs.append("")
    else:
        sub = impl(digits - 1)
        for s in sub:
            strs.append(f'0{s}')
        for s in sub:
            strs.append(f'1{s}')
    return strs

if __name__ == "__main__":
    permuteBinary(4)
