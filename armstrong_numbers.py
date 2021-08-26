def armstrong_number(number):
    sum_number = 0

    for n in str(number):
        sum_number += int(n) ** len(str(number))

    return sum_number == number


print(armstrong_number(1634))