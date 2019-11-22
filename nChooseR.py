def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n - 1)

def choose(n, r):
    num = factorial(n)
    denom = factorial(r) * factorial(n - r)
    return num / denom

running = True
while(running):
    try:
        n = int(input("Enter n (negative to quit): "))
        r = int(input("Enter r (negative to quit): "))
    except:
        n = -1
        r = -1
    running = n >= 0 and r >= 0
    if(running):
        print(choose(n, r))
