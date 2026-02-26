rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

def show_available_rooms():
    print("\nAvailable Rooms:")
    available = False
    for room, student in rooms.items():
        if student is None:
            print(f"Room {room}")
            available = True
    if not available:
        print("No rooms available")

def reserve_room():
    name = input("Enter student name: ")
    show_available_rooms()
    room_no = int(input("Enter room number to reserve: "))

    if room_no in rooms:
        if rooms[room_no] is None:
            rooms[room_no] = name
            print(f"Room {room_no} successfully reserved for {name}")
        else:
            print("Room already occupied")
    else:
        print("Invalid room number")

def cancel_reservation():
    room_no = int(input("Enter room number to cancel reservation: "))
    if room_no in rooms:
        if rooms[room_no] is not None:
            print(f"Reservation cancelled for {rooms[room_no]}")
            rooms[room_no] = None
        else:
            print("Room is already empty")
    else:
        print("Invalid room number")

def view_reservations():
    print("\nCurrent Reservations:")
    for room, student in rooms.items():
        if student is not None:
            print(f"Room {room}: {student}")
        else:
            print(f"Room {room}: Empty")

def main():
    while True:
        print("1. View Available Rooms")
        print("2. Reserve a Room")
        print("3. Cancel Reservation")
        print("4. View All Reservations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_available_rooms()
        elif choice == '2':
            reserve_room()
        elif choice == '3':
            cancel_reservation()
        elif choice == '4':
            view_reservations()
        elif choice == '5':
            print("Thank you for using the system")
            break
        else:
            print("Invalid choice. Try again.")

main()