def beerSong():
    for i in range(99, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        if i == 1:
            print(f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")

    print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n")

beerSong()