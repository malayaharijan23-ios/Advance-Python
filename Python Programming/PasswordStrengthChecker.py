def check_password(password):
    str=0
    if len(password)>=8:
        str=str+1
    if any(char.isupper() for char in password):
        str=str+1
    if any(char.islower() for char in password):
        str=str+1
    if any(char.isdigit() for char in password):
        str=str+1
    special="!@#$%^&*()_+-="
    if any(char in special for char in password):
        str=str+1
    if str<=2:
        print("Weak Password")
    elif str==3 or str==4:
        print("Medium Password ")
    else:
        print("Strong Password")
password = input("Enter Password: ")
check_password(password)