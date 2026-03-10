inventory = {}          
movement_history = {}   


def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter initial quantity: "))

    inventory[name] = inventory.get(name, 0) + qty
    movement_history.setdefault(name, [])
    print("Item added successfully.")

def track_movement():
    name = input("Enter item name: ")

    if name not in inventory:
        print("Item not found.")
        return

    print("1. Stock In")
    print("2. Stock Out")
    choice = input("Choose movement type: ")

    qty = int(input("Enter quantity: "))

    if choice == "1":
        inventory[name] += qty
        print("Stock added.")
    elif choice == "2":
        if qty <= inventory[name]:
            inventory[name] -= qty
            movement_history[name].append(qty)
            print("Stock removed.")
        else:
            print("Not enough stock.")
    else:
        print("Invalid choice.")


def inventory_report():
    print("\n--- Inventory Report ---")
    for item, qty in inventory.items():
        print(f"{item}: {qty} units")


def forecast_demand():
    name = input("Enter item name: ")

    if name not in movement_history or len(movement_history[name]) == 0:
        print("Not enough data to forecast.")
        return

    avg_demand = sum(movement_history[name]) / len(movement_history[name])
    print(f"Average demand for {name}: {avg_demand:.2f} units per sale")

def main():
    while True:
        print("\n===== Warehouse Automation System =====")
        print("1. Add Item")
        print("2. Track Goods Movement")
        print("3. Inventory Report")
        print("4. Forecast Demand")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            track_movement()
        elif choice == "3":
            inventory_report()
        elif choice == "4":
            forecast_demand()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

main()