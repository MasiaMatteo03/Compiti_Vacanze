def sum_of_multiples(number):
    list_multiples = []

    for count in range(1, number):
        if count % 3 == 0 or count % 5 == 0:

            list_multiples.append(count)

    return list_multiples, sum(list_multiples)


print(sum_of_multiples(20))