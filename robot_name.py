import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def robot_name():
    random_letters = ""
    random_numbers = ""

    for _ in range(0, 2):
        random_letters += letters[random.randint(0, len(letters) - 1)]

    for _ in range(0, 3):
        random_numbers += str(random.randint(0, 9))

    return random_letters + random_numbers

print(robot_name())