values = {}

def word_count(string):

    for word in string.split():

        word = word.lower()

        if not word in values:
            values[word] = 1

        else:
            values[word] += 1

    return values


print(word_count("ciao viva ciao prova"))
