def transpose(row1, row2):
    string_final = ""

    if len(row1) > len(row2):
        row2 += "-"
        
    elif len(row2) > len(row1):
        row1 += "-"

    for count in range(len(row1)):
        string_final += row1[count] + row2[count] + "\n"

    return string_final


print(transpose("ab", "def"))