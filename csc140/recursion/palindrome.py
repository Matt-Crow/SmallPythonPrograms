
def isPalindrome(s):
    print(s)
    """
           empty string
                           start = end
                                                     everything between start and end is a palindrome
    """
    return len(s) == 0 or (s[0] == s[len(s) - 1] and isPalindrome(s[1:len(s) - 1]))


if __name__ == "__main__":
    words = [
        "tacocat",
        "doug",
        "incorrect",
        "hello hello",
        "taco cat"
    ]

    for word in words:
        if isPalindrome(word):
            print(f'{word} is a palindrome')
        else:
            print(f'{word} is not a palindrome')
