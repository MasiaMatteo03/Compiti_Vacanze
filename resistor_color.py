def resistor_color(color1, color2):
    res_value = ""
    colors = {"Black": 0,
              "Brown": 1,
              "Red": 2,
              "Orange": 3,
              "Yellow": 4,
              "Green": 5,
              "Blue": 6,
              "Violet": 7,
              "Grey": 8,
              "White": 9}

    res_value += str(colors[color1]) + str(colors[color2])


    return res_value 

print(resistor_color("Red", "Black"))