import json

def search_customer():
    keyword = input("Enter name or phone to search: ").lower()

    with open("customers.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    matches = [c for c in data if keyword in c["name"].lower() or keyword in c["phone"]]

    if matches:
        print(f"🔍 Found {len(matches)} customer(s):")
        print("----------------------------")
        for index, customer in enumerate(matches, start=1):
            print(f"{index}. Name: {customer['name']}")
            print(f"   Phone: {customer['phone']}")
            print(f"   Email: {customer['email']}")
            print("----------------------------")
    else:
        print("❌ No customer found with that keyword.\n")
