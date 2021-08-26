def rna_transcription(dna):
    rna_string = ""
    for letter in dna:
        if letter == "G":
            rna_string += "C"
        
        elif letter == "C":
            rna_string += "G"

        elif letter == "T":
            rna_string += "A"
        
        elif letter == "A":
            rna_string += "U"

    return rna_string

def main():
    dna = input("Insert an DNA strand (use only these letters: G-C-T-A) >>>")

    print(f"RNA: {rna_transcription(dna)}")

if __name__ == "__main__":
    main()