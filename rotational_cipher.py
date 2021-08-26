def rotational_cipher(string, offset):
    strRot = ""
    string = string.lower()
    for element in string:
        if element == " ":
            strRot = strRot + element
        else:

            element = ord(element) - ord('a')
            element = (element + offset) % 26
            element = element + ord('a')
            element = chr(element)
            strRot = strRot + element
            
    print(f"Text >>> {string}")
    return strRot

print(rotational_cipher("The quick brown fox jumps over the lazy dog", 13))