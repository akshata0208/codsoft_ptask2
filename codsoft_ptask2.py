class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts[name] = contact
        print(f"Contact '{name}' added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, contact in self.contacts.items():
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    def search_contact(self, keyword):
        results = []
        for name, contact in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in contact['phone_number']:
                results.append(contact)
        return results

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone_number:
                contact['phone_number'] = new_phone_number
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for result in results:
                    print(f"Name: {result['name']}, Phone: {result['phone_number']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number (press Enter to skip): ")
            new_email = input("Enter new email (press Enter to skip): ")
            new_address = input("Enter new address (press Enter to skip): ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
