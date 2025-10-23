import json

def update_customer():
    keyword = input("Enter name or phone of the customer to update: ").lower()

    with open("customers.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    matches = [c for c in data if keyword in c["name"].lower() or keyword in c["phone"]]

    if not matches:
        print("❌ No customer found with that keyword.\n")
        return

    print(f"🔍 Found {len(matches)} customer(s):")
    for index, customer in enumerate(matches, start=1):
        print(f"{index}. Name: {customer['name']}")
        print(f"   Phone: {customer['phone']}")
        print(f"   Email: {customer['email']}")
        print("----------------------------")

    try:
        choice = int(input("Enter the number of the customer to update: "))
        if choice < 1 or choice > len(matches):
            print("❌ Invalid number.\n")
            return
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    customer = matches[choice - 1]

    new_name = input(f"Enter new name ({customer['name']}): ")
    new_phone = input(f"Enter new phone ({customer['phone']}): ")
    new_email = input(f"Enter new email ({customer['email']}): ")

    if new_name:
        customer['name'] = new_name
    if new_phone:
        customer['phone'] = new_phone
    if new_email:
        customer['email'] = new_email

    with open("customers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Customer ({customer['name']}) updated successfully!\n")
