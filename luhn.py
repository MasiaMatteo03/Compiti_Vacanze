def luhn(number):
    sumNumbers = 0

    numberSost = str(number).split()        #number sostitutivo trasformato da stringa a lista per eliminare gli spazi

    numberString = ""
        
    for i in numberSost:        #metto nella stringa i numeri della lista senza spazi
        numberString += i

    for n in range(0, len(numberString), 2):

        if ((int(numberString[n]) * 2) > 9):
            sumNumbers += (int(numberString[n]) * 2) - 9
        
        else:
            sumNumbers += int(numberString[n]) * 2

    for n in range(1, len(numberString), 2):
        
        sumNumbers += int(numberString[n])

    
    return sumNumbers % 10 == 0


print(f"Your number is valid? >>{luhn('4539 1488 0343 6467')}")