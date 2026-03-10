students = []     
courses = []     
while True:
    print("\nCollege Management System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Mark Attendance")
    print("5. Add Marks")
    print("6. Assign Grade")
    print("7. View Student Report")
    print("8. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        student = {
            "id": sid,
            "name": name,
            "courses": [],       
            "attendance": {},    
            "marks": {},
            "grade": {}
        }
        students.append(student)
        print("Student Added Successfully")
    elif choice == "2":
        cid = input("Enter Course ID: ")
        cname = input("Enter Course Name: ")
        course = {"cid": cid, "cname": cname}
        courses.append(course)
        print("Course Added Successfully")
    elif choice == "3":
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        student_found = None
        course_found = None
        for s in students:
            if s["id"] == sid:
                student_found = s
        for c in courses:
            if c["cid"] == cid:
                course_found = c
        if student_found and course_found:
            student_found["courses"].append(course_found["cname"])
            student_found["attendance"][cid] = set()
            print("Student Enrolled Successfully")
        else:
            print("Student or Course Not Found")
    elif choice == "4":
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        day = input("Enter Attendance Day: ")
        for s in students:
            if s["id"] == sid and cid in s["attendance"]:
                s["attendance"][cid].add(day)  
                print("Attendance Marked")
    elif choice == "5":
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        mark = int(input("Enter Marks: "))
        for s in students:
            if s["id"] == sid:
                s["marks"][cid] = mark
                print("Marks Added")
    elif choice == "6":
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        for s in students:
            if s["id"] == sid and cid in s["marks"]:
                mark = s["marks"][cid]
                if mark >= 90:
                    grade = "A"
                elif mark >= 75:
                    grade = "B"
                elif mark >= 50:
                    grade = "C"
                else:
                    grade = "Fail"
                s["grade"][cid] = grade
                print("Grade Assigned")
    elif choice == "7":
        sid = input("Enter Student ID: ")

        for s in students:
            if s["id"] == sid:
                print("\nStudent Name:", s["name"])
                for cid in s["attendance"]:
                    print("\nCourse ID:", cid)
                    print("Attendance Days:", len(s["attendance"][cid]))
                    print("Marks:", s["marks"].get(cid, "Not Added"))
                    print("Grade:", s["grade"].get(cid, "Not Assigned"))
    elif choice == "8":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")
