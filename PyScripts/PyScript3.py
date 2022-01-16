Contact = {}
choice =0
while True:
    print("1. Insert Contact: ")
    print("2. View Contacts: ")
    print("3. Search Contact by name: ")
    print("4. Search by key")
    choice= int(input())

    #Insert
    if choice == 1:
        phone_num = input("Enter Phone number: ")
        contact_name = input("Enter name to save contact: ")
        Contact.update({contact_name:phone_num})

    elif choice == 2:
        for num , nm in Contact.items():
            print(num,"-->",nm)
    elif choice == 3:
        name = input("Enter name to search: ")
        if name in Contact:
            print(name+"-->"+Contact[name])
    elif choice == 4:
        key_word = input("Enter key word to search")
        for name in Contact.keys():
            if key_word in name:
                print(name+"-->"+Contact[name])

    else:
        break



