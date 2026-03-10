def deposit(balance,transactions):
    amount=int(input("Enter deposit amount: "))
    if amount>0:
        balance=balance+amount
        transactions.append(amount)
        print(amount,"deposited successfully.")
    else:
        print("Invalid amount.")
    return balance
def withdraw(balance, transactions):
    amount=int(input("Enter withdrawal amount: "))
    if 0<amount<=balance:
        balance=balance-amount
        transactions.append(-amount)
        print(amount,"withdraw successfully.")
    else:
        print("Invalid amount.")
    return balance
def check_balance(balance):
    print("Current balance:",balance)
def view_transactions(transactions):
    if transactions:
        print("Transaction History:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions yet.")

balance=0
transactions=[]
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice=='1':
        balance=deposit(balance, transactions)
    elif choice=='2':
         balance = withdraw(balance, transactions)
    elif choice == '3':
        check_balance(balance)
    elif choice == '4':
        view_transactions(transactions)
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice.")

