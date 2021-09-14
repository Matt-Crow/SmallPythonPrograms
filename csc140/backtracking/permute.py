"""
permute(s): returns all possible possible arangements of characters in s
"""

def permute(s):
    if(len(s) is 0):
        return []

    chars = [char for char in s]
    return permImpl(chars)

def permImpl(chars):
    # base case
    if(len(chars) is 1):
        return chars

    perms = []
    for charNum in range(0, len(chars)):
        charsDupe = []
        for i in range(0, len(chars)):
            if i is not charNum:
                charsDupe.append(chars[i])
        # charsDupe now contains all chars except chars[charNum]
        """
        choose chars[charNum], then recursively call to get all permutations of
        the remaining characters. Note that the remaining characters are fewer
        than the parameter this was passed, so this converges to the base case.
        """
        for perm in permImpl(charsDupe): # has one less element than this call
            perms.append(chars[charNum] + perm)
    return perms


if __name__ == "__main__":
    word = "abcd"
    p = permute(word)
    print(f'Permutations of "{word}":')
    for perm in p:
        print(perm)
    print(f'=== {len(p)} permutations ===')
