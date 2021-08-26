def protein_translation(rna):
    final_codon = ""
    codon = ""
    proteins = []

    for counter in range (1, len(rna) + 1, 1):  #parte da 1 se no 0 % 3 == 0, counter - 1 perchè se no string index out of range
        final_codon += rna[counter - 1]
        codon += rna[counter - 1]

        if counter % 3 == 0:
            final_codon += " "
            
            if codon == "AUG":
                proteins.append("Methionine")
            
            elif codon == "UUU" or codon == "UUC":
                proteins.append("Phenylalanine")

            elif codon == "UUA" or codon == "UUG":
                proteins.append("Leucine")

            elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
                proteins.append("Serine")

            elif codon == "UAU" or codon == "UAC":
                proteins.append("Tyrosine")

            elif codon == "UGU" or codon == "UGC":
                proteins.append("Cysteine")

            elif codon == "UAA" or codon == " UAG" or codon == "UGA":
                continue
            
            codon = ""

    return final_codon, proteins


print(protein_translation("AUGUUUUCUUAAAUG"))