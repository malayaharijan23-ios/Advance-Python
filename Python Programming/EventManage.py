from datetime import datetime
entered_student = {}
rejected_student = {}

def enter_student():
    name=input("Enter Student name to enter: ")
    name=name.lower().replace(" ", "")
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entered_student[name] = time
    print(name,"has entered the event at",time)

def reject_student():
    name=input("Enter Student name to reject: ")
    name=name.lower().replace(" ", "")
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rejected_student[name] = time
    print(name,"has been rejected at",time)

def view_entered_students():
    print("\nEntered Students:")
    if entered_student:
        for name, time in entered_student.items():
            print(name, "-", time)
    else:
        print("No students entered.")

def view_rejected_students():
    print("\nRejected Students:")
    if rejected_student:
        for name, time in rejected_student.items():
            print(name, "-", time)
    else:
        print("No students rejected.")
        
def menu():
    while True:
        print("\n1. Enter Student")
        print("2. Reject Student")
        print("3. View Entered Students")
        print("4. View Rejected Students")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            enter_student()
        elif choice == 2:
            reject_student()
        elif choice == 3:
            view_entered_students()
        elif choice == 4:
            view_rejected_students()
        elif choice == 5:
            print("Break the Loop")
            break
        else:
            print("Invalid Choice! Please try again.")
menu()