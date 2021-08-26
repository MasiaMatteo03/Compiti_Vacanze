def collatz_conjecture(number):
    steps_count = 0

    while number != 1:
        
        if number % 2 == 0:
            number = number / 2
            steps_count += 1

        else:
            number = (number * 3) + 1
            steps_count += 1

    
    return steps_count


print(collatz_conjecture(12))