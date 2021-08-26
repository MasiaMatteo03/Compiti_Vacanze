def leap_year(year):
    ok = False

    if year % 4 == 0:
        ok = True

        if year % 100 == 0:
            ok = False

            if year % 400 == 0:
                ok = True
                
    else:
        ok = False


    return ok

print(leap_year(2000))
