import random

def value(random_numb):
    ability = 0

    for _ in range(0, 3):
        ability += max(random_numb)
        random_numb.remove(max(random_numb))

    return ability

def dnd_character():
    count_abilities = 1
    random_numb = []

    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    constitution_modifier = 0
    hitpoint = 10

    while count_abilities <= 6:
        for _ in range(0, 4, 1):
            random_numb.append(random.randint(1, 6))

        if count_abilities == 1:

            strength = value(random_numb)
            random_numb = []
            print(f"Strength: {strength}")

        elif count_abilities == 2:

            dexterity = value(random_numb)
            random_numb = []
            print(f"Dexterity: {dexterity}")

        elif count_abilities == 3:

            constitution = value(random_numb)
            random_numb = []
            print(f"Constitution: {constitution}")

        elif count_abilities == 4:

            intelligence = value(random_numb)
            random_numb = []
            print(f"Intelligence: {intelligence}")

        elif count_abilities == 5:

            wisdom = value(random_numb)
            random_numb = []
            print(f"Wisdom: {wisdom}")

        elif count_abilities == 6:

            charisma = value(random_numb)
            random_numb = []
            print(f"Charisma: {charisma}")
        
        count_abilities += 1

    constitution_modifier = round((constitution - 10) / 2)

    print(f"\nConstitution modifier: {constitution_modifier}")

    hitpoint += constitution_modifier
    
    print(f"Hitpoints: {hitpoint}")


dnd_character()