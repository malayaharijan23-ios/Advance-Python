registered = set()
entered = set()

while True:
    choice = input("1:Register  2:Enter  3:Total  4:Exit -> ")

    if choice == "1":
        name = input("Name: ").strip()
        if name in registered:
            print("Already registered")
        else:
            registered.add(name)
            print("Registered")

    elif choice == "2":
        name = input("Name: ").strip()
        if name not in registered:
            print("Not registered")
        elif name in entered:
            print("Fraud detected")
        else:
            entered.add(name)
            print("Entered")

    elif choice == "3":
        print(len(entered))

    elif choice == "4":
        break