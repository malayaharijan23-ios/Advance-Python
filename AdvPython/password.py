p=input("Enter password: ")
if len(p)<8:
    print("Password should be at least 8 characters.")
elif not any(c.isupper() for c in p):
    print("Password must contain at least one uppercase letter.")
elif not any(c.islower() for c in p):
    print("Password must contain at least one lowercase letter.")
elif not any(c.isdigit() for c in p):
    print("Password must contain at least one digit.")
elif not any(c in "!@#$%^&*" for c in p):
    print("Password must contain at least one special character")
else:
    print("Password is valid.")