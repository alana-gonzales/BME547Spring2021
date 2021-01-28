def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ") # input will always return a string
        if choice == "9":
            return

interface()