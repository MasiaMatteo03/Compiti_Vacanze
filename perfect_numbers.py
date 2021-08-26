def perfect_number(number):
    sumFact = 0
    for div in range(1, int(number / 2) + 1):
        if number % div == 0:
            sumFact += div

    if sumFact == number:
        return "Perfect number"

    elif sumFact > number:
        return "Abundant number"

    elif sumFact < number:
        return "Deficient number"


print(perfect_number(28))