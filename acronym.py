def acronym(string_acro):

    acronym_final = ""
    for word in string_acro.split(" "):
        acronym_final += word[0].upper()
    return acronym_final

def main():
    string = "prova di questo esercizio"

    print(f"The string is: {string}")
    print(f"The acronym is: {acronym(string)}")

if __name__ == "__main__":
    main()