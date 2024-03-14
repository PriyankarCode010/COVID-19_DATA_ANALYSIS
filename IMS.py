data = {
    "medicines": {},
    "e_items": {
        "laptops": {},          #default data
        "smartphone": {},
        "accessories": {}
    },
    "grocery": {}
}
while True:
    print("\n","*"*5,"OPERATIONS","*"*5)
    ch=input("1. ADD\n2. REMOVE\n3. DISPLAY\n4. SEARCH\n5. UPDATE\n6. Exit\nEnter you choice : ")
    if ch=="1":
        while True:
            print("\n","*"*5,"Add Product","*"*5)
            ch_2=input("1. medicies\n2. e_items\n3. grocery\nEnter the category : ")
            if ch_2=="1":
                print("\n","*"*5,"Medicies","*"*5)
                pro_ID=input("Enter the Product ID : ")
                pro_name=input("Enter Product name : ")
                quantity=int(input("Enter Quantity : "))
                price=int(input("Enter price per unit : "))
                expiry_date=input("Enter Expiry date : ")
                data["medicines"][pro_ID]={"name":pro_name,"quantity":quantity,"price":price,"Expiry_date":expiry_date}

            
            elif ch_2=="2":
                print("\n","*"*5,"E-Items","*"*5)
                ca={1:"laptops",2:"smartphone",3:"accessories"}
                print("1. Laptop 2.Smartphone 3. Accessories")
                cat=ca.get(int(input("Enter your choice : ")))
                pro_ID=input("Enter the Product ID : ")
                pro_name=input("Enter Product name : ")
                quantity=int(input("Enter Quantity : "))
                price=int(input("Enter price per unit : "))
                data["e_items"][cat][pro_ID]={"name":pro_name,"quantity":quantity,"price":price}
                
            elif ch_2=="3":
                print("\n","*"*5,"Grocery","*"*5)
                pro_ID=input("Enter the Product ID : ")
                pro_name=input("Enter Product name : ")
                quantity=int(input("Enter Quantity : "))
                price=int(input("Enter price per unit : "))
                expiry_date=input("Enter Expiry date : ")
                data["grocery"][pro_ID]={"name":pro_name,"quantity":quantity,"price":price,"Expiry_date":expiry_date}
            else:    
                print("\nInvalid input")
            print(pro_name,"added in data... ")
            print("\n")
            exit=input("Do you want to exit ADD section press -- (Y) : ")
            if exit.lower()=="y":
                break
    elif ch == "2":
        while True:
            print("\n","*"*5,"Remove Product","*"*5)
            ch_2 = input("1. medicines\n2. e_items\n3. grocery\nEnter the category to remove from: ")

            if ch_2 == "1":
                print("*" * 5, "Medicines", "*" * 5)
                pro_ID = input("Enter the Product ID to remove: ")
                if pro_ID in data["medicines"]:
                    del data["medicines"][pro_ID]
                    print("\nProduct removed successfully.")
                else:
                    print("\nProduct ID not found.")

            elif ch_2 == "2":
                print("*" * 5, "E-Items", "*" * 5)
                ca = {1: "laptops", 2: "smartphones", 3: "accessories"}
                print("1. Laptop 2.Smartphone 3. Accessories")
                cat = ca.get(int(input("Enter your choice: ")))
                pro_ID = input("Enter the Product ID to remove: ")
                if pro_ID in data["e_items"].get(cat, {}):
                    del data["e_items"][cat][pro_ID]
                    print("Product removed successfully.")
                else:
                    print("Product ID not found.")

            elif ch_2 == "3":
                print("*" * 5, "Grocery", "*" * 5)
                pro_ID = input("Enter the Product ID to remove: ")
                if pro_ID in data["grocery"]:
                    del data["grocery"][pro_ID]
                    print("Product removed successfully.")
                else:
                    print("Product ID not found.")
            else:
                print("\nInvalid input")
            
            print("\n")
            exit = input("Do you want to exit REMOVE section? Press -- (Y): ")
            if exit.lower() == "y":
                break
    elif ch == "3":
        print("\n","*" * 5, "DISPLAY", "*" * 5)

        print("Medicines:")
        if data["medicines"]:
            print("Product ID\tName\tQuantity\tPrice\tExpiry Date")
            for pro_ID, details in data["medicines"].items():
                print(f"{pro_ID}\t\t{details.get('name', '')}\t{details.get('quantity', '')}\t\t{details.get('price', '')}\t{details.get('Expiry_date', '')}")
        else:
            print("No medicines available.")
        print("*"*70)
        print("\nElectronic Items:")
        for cat, items in data["e_items"].items():
            print("\n")
            print(f"{cat}:")
            if items:
                print("Product ID\tName\tQuantity\tPrice")
                for pro_ID, details in items.items():
                    print(f"{pro_ID}\t\t{details.get('name', '')}\t{details.get('quantity', '')}\t\t{details.get('price', '')}")
            else:
                print("No items available.")
        print("*"*70)
        print("\nGrocery:")
        if data["grocery"]:
            print("Product ID\tName\tQuantity\tPrice\tExpiry Date")
            for pro_ID, details in data["grocery"].items():
                print(f"{pro_ID}\t\t{details.get('name', '')}\t{details.get('quantity', '')}\t\t{details.get('price', '')}\t{details.get('Expiry_date', '')}")
        else:
            print("No grocery items available.")
    elif ch == "4":
        print("\n","*"*5,"Search Product","*"*5)
        search_key = input("Enter the product ID to search: ")
        found = False
        for category, items in data.items():
            for item_ID, details in items.items():
                if search_key == item_ID:
                    print("Product found in", category, ":", details)
                    found = True
                    break
            if found:
                break
        else:
            print("Product ID not found.")
    
    elif ch == "5":
        print("\n","*" * 5, "UPDATE", "*" * 5)
        update_key = input("Enter the product ID to update: ")
        for category, items in data.items():
            if update_key in items:
                print("Product found in", category)
                new_name = input("Enter the new name (press Enter to keep the current name): ")
                if new_name:
                    items[update_key]["name"] = new_name
                new_quantity = input("Enter the new quantity (press Enter to keep the current quantity): ")
                if new_quantity:
                    items[update_key]["quantity"] = int(new_quantity)
                new_price = input("Enter the new price (press Enter to keep the current price): ")
                if new_price:
                    items[update_key]["price"] = int(new_price)
                print("Product updated successfully.")
                break
        else:
            print("Product ID not found.")
    elif ch=="6":
        print("THANK YOU......\n")
        break
    else:
        print("invalid input\n")