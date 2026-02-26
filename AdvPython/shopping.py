c = {}
while True:
    print("1.Add 2.Remove 3.Show 4.Total 5.Exit")
    ch = input("Enter: ")
    if ch == "1":
        n = input("Item: ")
        p = float(input("Price: "))
        q = int(input("Qty: "))
        c[n] = [p, q]
    elif ch == "2":
        n = input("Item: ")
        if n in c:
            del c[n]
    elif ch == "3":
        for i in c:
            print("Item=",i,"\nPrice= ",c[i][0],"\nQuantity= ", c[i][1])
    elif ch == "4":
        t = 0
        for i in c:
            t += c[i][0] * c[i][1]
        print("Total:", t)
    elif ch == "5":
        break