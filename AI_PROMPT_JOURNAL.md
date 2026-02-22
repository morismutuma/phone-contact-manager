# AI Prompt Journal - Phone Contact Manager

## Prompt 1: Project Structure & Data Design

Prompt Used:
I want to build a phone contact manager in Python. It should add, view, search, edit, and delete contacts. What's the best data structure to store contacts - a dictionary or list of dictionaries?

AI Response Summary:
Recommended list of dictionaries. Each contact is a dictionary with keys: id, name, phone, email, category. The list holds all contacts. This allows easy filtering, searching, and modification. IDs should be unique strings.

Code Applied:
```python
contact = {
    "id": generate_id(),
    "name": name,
    "phone": phone,
    "email": email,
    "category": category
}
contacts.append(contact)


Evaluation: ⭐⭐⭐⭐⭐
Critical decision - I initially thought one big dictionary with names as keys would work, but AI explained that lists allow duplicate names (two people named John) and easier iteration. Saved me from refactoring later.





Prompt 2: Phone Number Validation

Prompt Used:
How do I validate that a user enters only digits for a phone number in Python, minimum 10 characters? I need to keep asking until they enter valid input.

AI Response Summary:
Use .isdigit() method and len(). Strip spaces/dashes first with .replace(). Use a while True loop to keep asking until valid, then return.

Code Applied:

def get_valid_phone():
    while True:
        phone = input("Enter phone: ").strip()
        phone = phone.replace(" ", "").replace("-", "")
        if phone.isdigit() and len(phone) >= 10:
            return phone
        print("Invalid! Use 10+ digits.")

Evaluation: ⭐⭐⭐⭐⭐
Essential for data quality. Prevents app crashes from bad input and ensures clean data storage.




Prompt 3: Partial Name Search

Prompt Used:
How can I search contacts by name where typing 'John' finds both 'John Doe' and 'Johnny Smith'? I need case-insensitive partial matching.

AI Response Summary:
Convert both search term and stored names to lowercase using .lower(), then use in operator for partial matching. Use list comprehension to filter.

Code Applied:

def search_contact():
    search_term = input("Enter name: ").strip().lower()
    contacts = load_contacts()
    matches = [c for c in contacts if search_term in c["name"].lower()]


Evaluation: ⭐⭐⭐⭐⭐
Made the search user-friendly. Exact matches would be too rigid for real-world use.


Prompt 4: Editing/Updating Data

Prompt Used:
How do I update a specific contact in a list of dictionaries and save it back to file? I need to find by ID, modify fields, and persist changes.

AI Response Summary:
Find by ID using next() with generator expression. Modify the dictionary fields. Then overwrite entire file with updated list using save_contacts() function.

Code Applied:

def edit_contact():
    contact_id = input("Enter ID: ").strip()
    contacts = load_contacts()
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if contact:
        contact["name"] = new_name or contact["name"]
        save_contacts(contacts)  # Rewrite file

Evaluation: ⭐⭐⭐⭐
Works well for small files. AI noted this is fine for beginners, but production apps use databases with UPDATE statements for efficiency.



Prompt 5: Delete with Confirmation

Prompt Used:
How do I ask for user confirmation before deleting something in Python CLI? I want to prevent accidental deletions.

AI Response Summary:
Use input() with clear warning message. Check for "yes" (case-insensitive using .lower()). Use list comprehension to filter out deleted item, then save.

Code Applied:

def delete_contact():
    confirm = input(f"Delete '{contact['name']}'? (yes/no): ").lower()
    if confirm == "yes":
        contacts = [c for c in contacts if c["id"] != contact_id]
        save_contacts(contacts)
        print("Deleted!")
    else:
        print("Cancelled.")

Evaluation: ⭐⭐⭐⭐⭐
Good UX practice. The confirmation step prevents accidental data loss.


Therefor the reflection is:
Using AI prompts accelerated my learning significantly. Instead of reading entire documentation chapters, I got targeted solutions for specific problems:
Time saved: 2 hours vs searching Stack Overflow
Code quality: Learned Pythonic patterns like list comprehensions and next()
Understanding: AI explained WHY certain approaches work, not just HOW