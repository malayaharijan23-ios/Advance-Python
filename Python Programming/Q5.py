freelancers = {}
clients = {}
projects = []

def register_freelancer():
    fid = input("Enter Freelancer ID: ")
    name = input("Enter Freelancer Name: ")
    skill = input("Enter Skill: ")

    freelancers[fid] = {"name": name, "skill": skill, "earnings": 0}
    print("Freelancer registered successfully.")

def register_client():
    cid = input("Enter Client ID: ")
    name = input("Enter Client Name: ")

    clients[cid] = {"name": name}
    print("Client registered successfully.")

def assign_project():
    pid = input("Enter Project ID: ")
    title = input("Enter Project Title: ")
    cid = input("Enter Client ID: ")
    fid = input("Enter Freelancer ID: ")
    budget = float(input("Enter Project Budget: "))

    if cid in clients and fid in freelancers:
        project = {
            "pid": pid,
            "title": title,
            "client": cid,
            "freelancer": fid,
            "budget": budget,
            "paid": False
        }
        projects.append(project)
        print("Project assigned successfully.")
    else:
        print("Invalid Client ID or Freelancer ID.")

def process_payment():
    pid = input("Enter Project ID for payment: ")

    for project in projects:
        if project["pid"] == pid:
            if not project["paid"]:
                fid = project["freelancer"]
                amount = project["budget"]
                freelancers[fid]["earnings"] += amount
                project["paid"] = True
                print("Payment processed successfully.")
                print("Freelancer Earnings:", freelancers[fid]["earnings"])
                return
            else:
                print("Payment already completed.")
                return

    print("Project not found.")

def view_data():
    print("\n--- Freelancers ---")
    for fid, info in freelancers.items():
        print(fid, info)

    print("\n--- Clients ---")
    for cid, info in clients.items():
        print(cid, info)

    print("\n--- Projects ---")
    for p in projects:
        print(p)

def main():
    while True:
        print("\n===== Freelancer Marketplace =====")
        print("1. Register Freelancer")
        print("2. Register Client")
        print("3. Assign Project")
        print("4. Process Payment")
        print("5. View All Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_freelancer()
        elif choice == "2":
            register_client()
        elif choice == "3":
            assign_project()
        elif choice == "4":
            process_payment()
        elif choice == "5":
            view_data()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

main()