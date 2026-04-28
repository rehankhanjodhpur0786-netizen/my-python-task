records = {}

while True:
    print("1.Add-qualification")  
    print("2.view-qualification")
    print("3.update-my-qualification")
    print("4.exit")
    
    choice = input("choice: ")

    if choice == "1":
        i = input("id: ")
        records[i] = {
            "name": input("name: "),
            "addr": input("address: "),
            "qual": input("qualification: "),
            "10": input("10th year: "),
            "12": input("12th year: ")
        }
        print("added")

    elif choice == "2":
        i = input("id: ")
        print(records[i] if i in records else "not found")

    elif choice == "3":
        i = input("id: ")
        if i in records:
            records[i]["name"] = input("name: ")
            records[i]["addr"] = input("address: ")
            records[i]["qual"] = input("qualification: ")
            records[i]["10"] = input("10th: ")
            records[i]["12"] = input("12th: ")
            print("your reord is compleate")
        else:
            print("not found")

    elif choice == "4":
        break