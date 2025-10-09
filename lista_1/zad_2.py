def is_palindrome(word):
    new_word = ""
    for c in word:
        if c.isalnum(): new_word += c.lower()
    if new_word == new_word[::-1]:
        return True
    else:
        return False
w = input("Enter a word: ")
print(is_palindrome(w))

def is_palindrom_2(word):
    new_word = "".join(c.lower() for c in word if c.isalnum())
    return new_word == new_word[::-1]
print(is_palindrom_2(w))