# 📱 Phone Contact Manager - Python Beginner's Toolkit

## 1. Title & Objective

**Technology Chosen:** Python 3.x Programming Language

**Why I Chose It:** Python has clean, readable syntax perfect for beginners. I wanted to build something practical that demonstrates CRUD operations (Create, Read, Update, Delete) which are fundamental to all software applications.

**End Goal:** Create a command-line phonebook application where users can add contacts, view all contacts, search by name, edit existing contacts, delete contacts, and view statistics.

---

## 2. Quick Summary of the Technology

**What is Python?**
Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability with its use of significant whitespace and English-like syntax.

**Where is it used?**
- Web development (Django, Flask)
- Data science & machine learning
- Automation & scripting
- Desktop applications

**Real-world example:** Instagram's backend handles millions of requests daily using Python and Django.

---

## 3. System Requirements

| Requirement         | Specification                   |
|-------------        |---------------                  |
| **OS**              | Linux (Kali), macOS, or Windows |
| **Python Version**  | Python 3.8 or higher            |
| **Editor**          | VS Code (pre-installed on Kali) |
| **Package Manager** | pip (comes with Python)         |

**Verify Installation:**
```bash```
```python3 --version ```

4. Installation & Setup Instructions
Step 1: Navigate to Project Directory
  ``` cd phone-contact-manager```

Step 2: Create Virtual Environment

 ```python3 -m venv venv```

Step 3: Activate Virtual Environment
 ```source venv/bin/activate```

Step 4: Run the Application
  ```python3 phonebook.py```
5. Minimal Working Example
What it does: A CLI phonebook with full CRUD functionality - add, view, search, edit, delete contacts with data persistence to file.
📸 Screenshots

| Feature             | Screenshot                                                                                                          |
| -------------       | --------------------------------------------------------------------------------------                              |
| Main Menu           | ![Menu](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/menu1.png)             |
| Add Contact         | ![Add](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/addcontact1.png)        |
| View Contacts       | ![View](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/viewcontact.png)       |
| Search              | ![Search](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/contactsearched.png) |
| Edit                | ![Edit](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/contactedited.png)     |
| Delete              | ![Delete](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/contactdeleted.png)  |
| Statistics          | ![Stats](https://raw.githubusercontent.com/morismutuma/phone-contact-manager/main/screenshots/statistics.png)       |


File Structure

phone-contact-manager/
├── phonebook.py          # Main application
├── contacts.txt          # Data file (auto-created)
├── screenshots/           # Application screenshots
│   ├── menu1.png
│   ├── addcontact1.png
│   ├── viewcontact.png
│   ├── contactsearched.png
│   ├── contactedited.png
│   ├── contactdeleted.png
│   └── statistics.png
├── README.md             # This file
└── AI_PROMPT_JOURNAL.md  # AI usage documentation

Run Instructions

  ```source venv/bin/activate ```
      ```python3 phonebook.py ```

Sample Session:

📱 PHONE CONTACT MANAGER
========================================
1. ➕ Add New Contact
2. 📋 View All Contacts
3. 🔍 Search Contact by Name
4. ✏️  Edit Contact
5. 🗑️  Delete Contact
6. 📊 Contact Statistics
7. 🚪 Exit
========================================

Select an option (1-7): 1

--- ➕ Add New Contact ---
Enter full name: John Doe
Enter phone number (digits only, 10+ chars): 0712345678
Enter email (or press Enter to skip): john@email.com

Categories: Family, Friend, Work, Emergency, Other
Enter category: Friend

✅ Contact added successfully!
   ID: 1
   Name: John Doe
   Phone: 0712345678

6. AI Prompt Journal
See AI_PROMPT_JOURNAL.md for detailed documentation of AI prompts used, responses, and learning reflections.
Summary of AI Assistance:
Prompt 1: Data structure design (list of dictionaries)
Prompt 2: Phone number validation logic
Prompt 3: Partial name search implementation
Prompt 4: Edit/update contact workflow
Prompt 5: Delete confirmation UX
Key Learning: AI accelerated development by providing targeted solutions instead of reading entire documentation chapters. Saved approximately 2 hours of research time.


7. Common Issues & Fixes

| Issue                                 | Error/Symptom                             | Solution                                                               |
| ------------------------------     | -----------------------------                | ---------------------------------------------------------------------- |
| **Permission Denied**              | `PermissionError: [Errno 13]`                | Use `python3 phonebook.py` instead of `./phonebook.py`                 |
| **Python not found**               | `command not found: python`                  | Use `python3` explicitly (Kali default)                                                        |
| **Virtual env not activating**     | `source: not found`                          | Run `bash` first, or use `. venv/bin/activate`                         |       
| **Search finds nothing**           | No results displayed                         | Check spelling - search is case-insensitive but checks exact substring |
| **Cannot edit contact**            | "Contact not found"                          | View contacts first to get correct ID number                           |
| **Phone validation fails**         | "Invalid phone number"                       | Remove spaces/dashes - digits only, minimum 10 characters              |

Kali Linux Specific:

# If python command defaults to Python 2, always use:
 ```python3 phonebook.py```

# Or create alias in ~/.bashrc:
 ```echo "alias python=python3" >> ~/.bashrc```
         ```source ~/.bashrc ```


8. References

Official Documentation
Python 3 Documentation   https://docs.python.org/3/
Python Tutorial                         https://docs.python.org/3/tutorial/

Learning Resources
Real Python - Tutorials and best practices                           https://realpython.com/ 
Automate the Boring Stuff - Practical Python projects  https://automatetheboringstuff.com/

Tools Used
VS Code - Code editor                                              https://code.visualstudio.com/
Python Tutor - Visualize code execution        https://pythontutor.com/


 Quick Start Commands

# 1. Enter project directory
```cd phone-contact-manager```

# 2. Activate virtual environment

```source venv/bin/activate```

# 3. Run application
```python3 phonebook.py```

# 4. Test the features:
#    - Add 2-3 contacts
#    - View all contacts
#    - Search by name
#    - Edit a contact
#    - Check statistics
#    - Delete a contact
#    - Exit

Submission Checklist
[x] Toolkit Document (README.md) - Complete
[x] AI Prompt Journal (AI_PROMPT_JOURNAL.md) - Complete
[x] Working Codebase (phonebook.py) - Tested and functional
[x] Setup instructions for Kali Linux - Included
[x] Common errors and solutions - Documented
[x] Reference resources - Listed
[x] Screenshots - 7 images included

Submitted by: Moris Mutuma
Date: 2026-02-22
Course: Moringa AI Capstone Project
