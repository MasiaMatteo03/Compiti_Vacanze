alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def pangram(sentence):
    for letter in sentence:
        letter = letter.lower()
        if letter ==  " ":
            continue
        else:
            if letter in alphabet:
                alphabet.remove(letter)
                
    
    if len(alphabet) == 0:
        return True
    else:
        return False



print(pangram("The quick brown fox jumps over the lazy dog"))