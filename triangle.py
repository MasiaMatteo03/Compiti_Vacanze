def triangle(side1, side2, side3):

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "You can't build a triangle with a side that has value of 0."
    else:
        if (side1 + side2) < side3 or (side1 + side3) < side2 or (side2 + side3) < side1:
            return "You can't build a triangle with this sides."
        
        else:
            if (side1 == side2 and side1 == side3 and side2 == side3):
                return "This triangle is equilateral."

            elif (side1 != side2 and side1 != side3 and side2 != side3):
                return "This triangle is scalene."

            else:
                return "This triangle is isosceles."


print(triangle(5, 5, 5))