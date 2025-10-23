import json

def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    customer = {"name": name, "phone": phone, "email": email}

    with open("customers.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(customer)

    with open("customers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Customer ({name}) added successfully!\n")
