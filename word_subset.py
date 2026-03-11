"""
word_subset.py

Prints all words which can be made using the letters in a given word.
"""



def print_subwords(prefix: str, other_letters: str, all_words: set[str]):
    # base case: exits if we have no other letters left to try
    for other_letter in set(other_letters): # use set to remove duplicates
        maybe_word = prefix + other_letter
        if maybe_word in all_words:
            print(maybe_word)
        
        # it may or may not be a word, but also check if it's a prefix for a word
        with_letter_removed = other_letters.replace(other_letter, "", 1)
        print_subwords(maybe_word, with_letter_removed, all_words)


word = input("Enter a word: ").lower()

with open("/usr/share/dict/words") as f:
    all_words = [line.strip().lower() for line in f.readlines() if line != ""]
    
search_me_for_matches = set(all_words)
print_subwords("", word, search_me_for_matches)