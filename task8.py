users = {}          
while True:
    print("1. registration")
    print("2. login")
    print("3. view all records")
    print("4. exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        print("registration page")
        name = input("enter your name: ")
        email = input("enter your email: ")
        password = input("enter yourt password: ")

        users[email] = [name, password]

        print("your registration form is successfully created")

    elif choice == 2:
        print("your login page")
        email = input("enter your email: ")
        password = input("enter your password: ")

        if email in users:
            if users[email][1] == password:
                print("your login successfully created")
            else:
                print("your password is not found")
        else:
            print("your email is not found")

    elif choice == 3:
        print("all records:")

        keys = list(users.keys())
        i = 0

        while i < len(keys):
            email = keys[i]

            print("name:", users[email][0])
            print("email:", email)
            print("password:", users[email][1])
            print("------")

            i += 1

    elif choice == 4:
        print("thank you")
        break

    else:
        print("invalid choice")