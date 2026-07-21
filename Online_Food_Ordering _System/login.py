def login():
    print("------LOGIN------")
    username = input("Enter username:")
    password = input("Enter password:")
    if username == "bhuvanes food court" and password == "1234":
        print("Login Successfull")
        return True
    else:
        print("Invalid username or password")
        return False