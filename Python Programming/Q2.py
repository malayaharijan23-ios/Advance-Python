customers = {}          
communications = {}     
sales = {}             


def add_customer():
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    customers[cid] = {
        "name": name,
        "phone": phone,
        "email": email
    }
    communications.setdefault(cid, [])
    sales.setdefault(cid, 0.0)

    print("Customer added successfully.")

def add_communication():
    cid = input("Enter Customer ID: ")

    if cid in customers:
        message = input("Enter communication note: ")
        communications[cid].append(message)
        print("Communication logged.")
    else:
        print("Customer not found.")


def add_sale():
    cid = input("Enter Customer ID: ")

    if cid in customers:
        amount = float(input("Enter sale amount: "))
        sales[cid] += amount
        print("Sale recorded successfully.")
    else:
        print("Customer not found.")


def view_customer():
    cid = input("Enter Customer ID: ")

    if cid in customers:
        print("\n--- Customer Info ---")
        print("Name:", customers[cid]["name"])
        print("Phone:", customers[cid]["phone"])
        print("Email:", customers[cid]["email"])

        print("\n--- Communications ---")
        for msg in communications[cid]:
            print("-", msg)

        print("\n--- Total Sales ---")
        print("₹", sales[cid])
    else:
        print("Customer not found.")


def view_all_customers():
    print("\n--- All Customers ---")
    for cid, info in customers.items():
        print(cid, info)


def main():
    while True:
        print("\n===== CRM System =====")
        print("1. Add Customer")
        print("2. Add Communication Log")
        print("3. Add Sale")
        print("4. View Customer Details")
        print("5. View All Customers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_communication()
        elif choice == "3":
            add_sale()
        elif choice == "4":
            view_customer()
        elif choice == "5":
            view_all_customers()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

main()