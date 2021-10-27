"""
given a file containing a set of characters and the number of occurences of each
of those characters, find a way of unambiguously encoding a string
"""



def test():
    myStr = "This is a test string for variable length encoding"
    print(myStr)
    cipher = getCipher(myStr)
    print(cipher)
    encoded = encode(myStr, cipher)
    print(encoded)
    decoded = decode(encoded, cipher)
    print(decoded)
    print(f'Compression: {len(myStr) * 8 / len(encoded)}')

def getCipher(str):
    charToFrequency = dict()
    for char in str:
        if char not in charToFrequency:
            charToFrequency[char] = 1
        else:
            charToFrequency[char] += 1

    entries = []

    for k, v in charToFrequency.items():
        entries.append((k, v))
    sortByValue(entries)

    cipher = dict()
    # no
    base = "1"
    for entry in entries:
        cipher[entry] = base
        base = "0" + base

    return cipher

def sortByValue(a):
    sortByValueImpl(a, 0, len(a))
    for i in range(0, len(a)):
        a[i] = a[i][0]

def sortByValueImpl(a, min, max):
    if max - min <= 1:
        return;

    mid = int((min + max) / 2)
    sortByValueImpl(a, min, mid)
    sortByValueImpl(a, mid, max)

    merged = []
    i = min
    j = mid
    while i < mid and j < max:
        if a[i][1] < a[j][1]:
            merged.append(a[j])
            j += 1
        else:
            merged.append(a[i])
            i += 1
    while i < mid:
        merged.append(a[i])
        i += 1
    while j < max:
        merged.append(a[j])
        j += 1

    for k in range(0, max - min):
        a[k + min] = merged[k]

def encode(str, cipher):
    result = ""
    for char in str:
        result += cipher[char]
    return result

def decode(str, cipher):
    inv = invertCipher(cipher)
    result = ""
    currToken = ""
    for char in str:
        if char == "1": # end of token
            currToken += "1"
            result += inv[currToken]
            currToken = ""
        else:
            currToken += "0"
    return result

def invertCipher(cipher):
    inv = dict()
    for k, v in cipher.items():
        inv[v] = k
    return inv

if __name__ == "__main__":
    test()
