def prime_factors(number):
    cont = 2
    factors = []

    while number != 1:
        if number % cont == 0:
            number = number / cont
            factors.append(cont)
        
        else:
            cont += 1

    return factors


print(prime_factors(10))