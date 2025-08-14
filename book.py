# Simple Contact Book in Python

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Found Contact → Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!")
    else:
        print("Contact not found.")

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye! Closing contact book.")
        break
    else:
        print("Invalid choice! Please enter 1-6.")
