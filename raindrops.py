def raindrops(number):
    string_rain = ""

    if number % 3 == 0:
        string_rain += "Pling"
    
    if number % 5 == 0:
        string_rain += "Plang"

    if number % 7 == 0:
        string_rain += "Plong"

    if len(string_rain) == 0:
        return f"The {number} doesn't have any of 3, 5, 7 as factor."

    else:
        return string_rain


print(raindrops(10))