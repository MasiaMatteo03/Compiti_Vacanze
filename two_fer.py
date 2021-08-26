def two_fer(name):
    print(f"One for {name}, one for me.\n")

def main():
    while True:
        name = input("Insert a name >>> ")

        if name == "":
            print("One for you, one for me.\n")

        elif name == "exit":
            print("Closing the program.")
            break

        else:
            two_fer(name)


if __name__ == "__main__":
    main()