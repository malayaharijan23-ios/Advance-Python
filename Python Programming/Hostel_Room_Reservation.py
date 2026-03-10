rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}
occupied = set()
while True:
    print("\n--- Hostel Room Reservation ---")
    print("1. View Room Status")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. View Occupied Rooms")
    print("5. Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        for room, student in rooms.items():
            if student is None:
                print(f"Room {room} : Available")
            else:
                print(f"Room {room} : Booked by {student}")
    elif choice=="2":
        room_no=int(input("Enter room number: "))
        if room_no in rooms:
            if rooms[room_no] is None:
                name=input("Enter student name: ")
                rooms[room_no]=name
                occupied.add(room_no)
                print("Room booked successfully")
            else:
                print("Room already occupied")
        else:
            print("Invalid room number")
    elif choice == "3":
        room_no = int(input("Enter room number to cancel: "))
        if room_no in rooms:
            if rooms[room_no] is not None:
                rooms[room_no] = None
                occupied.discard(room_no)
                print("Booking cancelled")
            else:
                print("Room already empty")
        else:
            print("Invalid room number")
    elif choice == "4":
        print("Occupied Rooms:", occupied)
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")
