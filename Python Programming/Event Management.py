from datetime import datetime
entered_student = {}
rejected_student = {}
while True:
    print("\n1. Enter Student")
    print("2. Reject Student")
    print("3. View Entered Students")
    print("4. View Rejected Students")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Student name to enter: ")
        name = name.lower().replace(" ", "")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entered_student[name] = time
        print(name, "has entered the event at", time)

    elif choice == 2:
        name = input("Enter Student name to reject: ")
        name = name.lower().replace(" ", "")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rejected_student[name] = time
        print(name, "has been rejected at", time)
    elif choice == 3:
        print("\nEntered Students:")
        for name, time in entered_student.items():
            print(name, "-", time)
    elif choice == 4:
        print("\nRejected Students:")
        for name, time in rejected_student.items():
            print(name, "-", time)
    elif choice == 5:
        print("Break the Loop")
        break
    else:
        print("Invalid Choice! Please try again.")
