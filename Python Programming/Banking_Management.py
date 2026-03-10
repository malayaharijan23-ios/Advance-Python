set_password = input("Create your password: ")
print("\n--- Login Required ---")
login_password = input("Enter your password to continue: ")

if login_password != set_password:
    print("Incorrect password. Access denied.")
else:
    print("Login successful!")

    balance = 0
    transactions = []

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                transactions.append(amount)
                print(amount, "deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive number.")

        elif choice == '2':
            amount = int(input("Enter withdrawal amount: "))
            if 0 < amount <= balance:
                balance -= amount
                transactions.append(-amount) 
                print(amount, "withdrawn successfully.")
            else:
                print("Invalid amount.")

        elif choice == '3':
            print("Current balance:", balance)

        elif choice == '4':
            if transactions:
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions yet.")

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
