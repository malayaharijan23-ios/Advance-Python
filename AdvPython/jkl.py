def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit amount: "))
    print("Account created successfully for", name)
    return balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid amount.")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
    return balance


def check_balance(balance):
    print("Current balance:", balance)


def main():
    balance = 0
    account_created = False

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            balance = create_account()
            account_created = True

        elif choice == '2':
            if account_created:
                balance = deposit(balance)
            else:
                print("Please create an account first.")

        elif choice == '3':
            if account_created:
                balance = withdraw(balance)
            else:
                print("Please create an account first.")

        elif choice == '4':
            if account_created:
                check_balance(balance)
            else:
                print("Please create an account first.")

        elif choice == '5':
            print("Thank you.")
            break

        else:
            print("Invalid choice.")


main()
