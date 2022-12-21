def is_palindrome(text):
    letters = []
    text = text.lower()
    text = text.split(" ")
    for word in text:
        for letter in word:
            letters.append(letter)

    text = "".join(letters)
    letters.reverse()
    letters_str_reverse = "".join(letters)

    if text == letters_str_reverse:
        return True

    return False


print(is_palindrome('Może jutro ta dama da tortu jeżom'))
