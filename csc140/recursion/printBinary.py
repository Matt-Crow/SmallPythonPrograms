

def printBinary(n):
    print(f'\n{n} = ', end = "")
    impl(n, 2)

def impl(n, base): # n >= 0, base > 1
    if n < base:
        print(n, end = "")
    else:
        impl(int(n / base), base)
        print(n % base, end = "")

if __name__ == "__main__":
    for i in range(0, 16):
        printBinary(i)
