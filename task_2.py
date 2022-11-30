def my_split(text):
    text_list = []
    word = ''
    for char in text:
        if char == " ":
            text_list.append(word)
            word = ''
        else:
            word += char
    if word:
        text_list.append(word)
    if text_list[0] == '':
        text_list.pop(0)

    return text_list


print(my_split(" Hobbit ma kota "))
