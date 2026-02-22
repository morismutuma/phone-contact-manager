#!/usr/bin/env python3
"""
Phone Contact Manager - A Beginner Python Project
Demonstrates: functions, conditionals, loops, file I/O, dictionaries, and list operations
"""

import os
import re

DATA_FILE = "contacts.txt"

def show_menu():
    """Display the main menu options."""
    print("\n" + "="*45)
    print("📱 PHONE CONTACT MANAGER")
    print("="*45)
    print("1. ➕ Add New Contact")
    print("2. 📋 View All Contacts")
    print("3. 🔍 Search Contact by Name")
    print("4. ✏️  Edit Contact")
    print("5. 🗑️  Delete Contact")
    print("6. 📊 Contact Statistics")
    print("7. 🚪 Exit")
    print("="*45)

def get_valid_phone():
    """Get and validate phone number input."""
    while True:
        phone = input("Enter phone number (digits only, 10+ chars): ").strip()
        # Remove any spaces or dashes
        phone = phone.replace(" ", "").replace("-", "")
        
        # Check if only digits and length >= 10
        if phone.isdigit() and len(phone) >= 10:
            return phone
        else:
            print("❌ Invalid phone number! Use 10+ digits only.")

def get_valid_email():
    """Get and validate email input."""
    while True:
        email = input("Enter email (or press Enter to skip): ").strip()
        
        if email == "":
            return "Not provided"
        
        # Simple email validation pattern
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            print("❌ Invalid email format! Try again or press Enter to skip.")

def load_contacts():
    """Load all contacts from file into a list of dictionaries."""
    contacts = []
    
    if not os.path.exists(DATA_FILE):
        return contacts
    
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line and "|" in line:
                parts = line.split("|")
                if len(parts) >= 4:
                    contact = {
                        "id": parts[0],
                        "name": parts[1],
                        "phone": parts[2],
                        "email": parts[3],
                        "category": parts[4] if len(parts) > 4 else "General"
                    }
                    contacts.append(contact)
    
    return contacts

def save_contacts(contacts):
    """Save all contacts back to file."""
    with open(DATA_FILE, "w") as file:
        for contact in contacts:
            line = f"{contact['id']}|{contact['name']}|{contact['phone']}|{contact['email']}|{contact['category']}\n"
            file.write(line)

def generate_id():
    """Generate a unique ID for new contact."""
    contacts = load_contacts()
    if not contacts:
        return "1"
    # Find max ID and increment
    max_id = max(int(c["id"]) for c in contacts)
    return str(max_id + 1)

def add_contact():
    """Add a new contact to the phonebook."""
    print("\n--- ➕ Add New Contact ---")
    
    name = input("Enter full name: ").strip().title()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    phone = get_valid_phone()
    email = get_valid_email()
    
    print("\nCategories: Family, Friend, Work, Emergency, Other")
    category = input("Enter category: ").strip().title() or "General"
    
    contact_id = generate_id()
    
    # Create contact dictionary
    new_contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }
    
    # Append to file
    with open(DATA_FILE, "a") as file:
        line = f"{new_contact['id']}|{new_contact['name']}|{new_contact['phone']}|{new_contact['email']}|{new_contact['category']}\n"
        file.write(line)
    
    print(f"\n✅ Contact added successfully!")
    print(f"   ID: {contact_id}")
    print(f"   Name: {name}")
    print(f"   Phone: {phone}")

def view_contacts():
    """Display all contacts in a formatted table."""
    print("\n--- 📋 All Contacts ---")
    
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found. Phonebook is empty!")
        return
    
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Category':<10} Email")
    print("-" * 75)
    
    for contact in contacts:
        # Format phone number nicely: 0712-345-678
        phone = contact["phone"]
        formatted_phone = f"{phone[:4]}-{phone[4:7]}-{phone[7:]}" if len(phone) >= 10 else phone
        
        print(f"{contact['id']:<5} {contact['name']:<20} {formatted_phone:<15} "
              f"{contact['category']:<10} {contact['email']}")

def search_contact():
    """Search contacts by name (partial match allowed)."""
    print("\n--- 🔍 Search Contact ---")
    
    search_term = input("Enter name to search: ").strip().lower()
    
    if not search_term:
        print("❌ Search term cannot be empty!")
        return
    
    contacts = load_contacts()
    matches = [c for c in contacts if search_term in c["name"].lower()]
    
    if not matches:
        print(f"No contacts found matching '{search_term}'")
        return
    
    print(f"\n✅ Found {len(matches)} contact(s):")
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Category':<10}")
    print("-" * 55)
    
    for contact in matches:
        phone = contact["phone"]
        formatted_phone = f"{phone[:4]}-{phone[4:7]}-{phone[7:]}" if len(phone) >= 10 else phone
        print(f"{contact['id']:<5} {contact['name']:<20} {formatted_phone:<15} {contact['category']:<10}")

def edit_contact():
    """Edit an existing contact."""
    print("\n--- ✏️  Edit Contact ---")
    
    view_contacts()
    print()
    
    contact_id = input("Enter ID of contact to edit: ").strip()
    
    contacts = load_contacts()
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    
    if not contact:
        print(f"❌ Contact with ID {contact_id} not found!")
        return
    
    print(f"\nEditing: {contact['name']}")
    print("Press Enter to keep current value, or type new value to change.")
    
    # Edit name
    new_name = input(f"Name [{contact['name']}]: ").strip()
    if new_name:
        contact["name"] = new_name.title()
    
    # Edit phone
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    if new_phone:
        if new_phone.isdigit() and len(new_phone) >= 10:
            contact["phone"] = new_phone
        else:
            print("❌ Invalid phone, keeping old number.")
    
    # Edit email
    new_email = input(f"Email [{contact['email']}]: ").strip()
    if new_email:
        if "@" in new_email:
            contact["email"] = new_email
        else:
            print("❌ Invalid email, keeping old email.")
    
    # Edit category
    new_category = input(f"Category [{contact['category']}]: ").strip()
    if new_category:
        contact["category"] = new_category.title()
    
    # Save back to file
    save_contacts(contacts)
    print(f"\n✅ Contact updated successfully!")

def delete_contact():
    """Delete a contact from the phonebook."""
    print("\n--- 🗑️  Delete Contact ---")
    
    view_contacts()
    print()
    
    contact_id = input("Enter ID of contact to delete: ").strip()
    
    contacts = load_contacts()
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    
    if not contact:
        print(f"❌ Contact with ID {contact_id} not found!")
        return
    
    confirm = input(f"⚠️  Are you sure you want to delete '{contact['name']}'? (yes/no): ").lower()
    
    if confirm == "yes":
        contacts = [c for c in contacts if c["id"] != contact_id]
        save_contacts(contacts)
        print(f"✅ Contact '{contact['name']}' deleted successfully!")
    else:
        print("Deletion cancelled.")

def show_statistics():
    """Show contact statistics."""
    print("\n--- 📊 Contact Statistics ---")
    
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts in phonebook.")
        return
    
    total = len(contacts)
    
    # Count by category
    categories = {}
    for c in contacts:
        cat = c["category"]
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"Total Contacts: {total}")
    print("\nBy Category:")
    print("-" * 25)
    for cat, count in sorted(categories.items()):
        percentage = (count / total) * 100
        bar = "█" * int(percentage / 5)  # Visual bar
        print(f"{cat:<12} {count:>3} ({percentage:>5.1f}%) {bar}")

def main():
    """Main application loop."""
    print("🚀 Welcome to Phone Contact Manager!")
    print("Your personal phonebook in Python.")
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\n👋 Goodbye! Thanks for using Phone Contact Manager!")
            break
        else:
            print("❌ Invalid option! Please choose 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()