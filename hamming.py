def hamming(string1, string2):
    hamming_distance = 0
    
    for i in range(len(string1)):
        if string2[i] != string1[i]:
            hamming_distance += 1
    
    return hamming_distance

def main():
    dna1 = "GAGCCTACTAACGGGAT"
    dna2 = "CATCGTAATGACGGCCT"

    print(f"Hamming distance: {hamming(dna1, dna2)}")


if __name__ == "__main__":
    main()