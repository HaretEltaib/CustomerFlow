import json

def show_all_customers():
    with open("customers.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print("📭 No customers found yet.\n")
        return

    print("📋 Customer List:")
    print("----------------------------")
    for index, customer in enumerate(data, start=1):
        print(f"{index}. Name: {customer['name']}")
        print(f"   Phone: {customer['phone']}")
        print(f"   Email: {customer['email']}")
        print("----------------------------")
