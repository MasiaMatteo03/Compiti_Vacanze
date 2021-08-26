def all_your_base(number, base):
    numberDecimal = 0
    counter = len(str(number)) - 1

    for c in str(number):
        numberDecimal += int(c) * base ** counter    #** -> elevato

        counter -= 1

    return numberDecimal


print(all_your_base(101010, 2))