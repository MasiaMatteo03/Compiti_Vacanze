def isogram(word):
    word = str(word)
    letters = list(word)

    while len(letters) != 0:
        temp = letters[0]

        letters.remove(letters[0])

        if temp in letters and (temp != " " or temp != "-"):
            return False

    return True


print(isogram("ciao"))