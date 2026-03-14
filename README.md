Phonebook CLI Application

A simple command-line phonebook application written in Python using Object-Oriented Programming (OOP).
The program allows users to store, search, edit, and delete contacts directly from the terminal.

This project is useful for beginners learning:

- Python classes
- Basic data structures
- User input handling
- Simple CLI program design

---

Author

GitHub: sakibh3330

---

Project Description

This program simulates a basic phonebook system.
Users can manage contacts through a simple menu interface.

The phonebook stores:

- Contact names
- Phone numbers

Contacts are stored using Python lists inside a class.

The application demonstrates how a class can be used to organize program logic and manage data.

---

Features

- Add new contacts
- Find contact by name
- Find contact by phone number
- Edit existing contact names
- Delete contacts
- Command-line menu interface
- Implemented using Python OOP concepts

---

Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Lists (basic data structure)
- Command Line Interface (CLI)

---

How the Program Works

When the program starts, it displays a menu:

1. Find number
2. Add number
3. Edit number
4. Delete number

The user selects an option and the program performs the requested operation.

Contact Storage Logic

The phonebook maintains two lists:

- "names" → stores contact names
- "numbers" → stores phone numbers

Both lists share the same index position, meaning:

Index| Name| Number
0| Alice| 123456
1| Bob| 987654

This allows the program to match names and numbers using the same index.

---

Example Usage

Example workflow:

Phonebook

1.Find number
2.Add number
3.Edit number
4.Delete number

Enter option: 2
Enter name: Alice
Enter number: 123456

Searching for a contact:

Enter option: 1
1.Name
2.Number

Enter name: Alice
123456

---

Project Structure

phonebook-project/
│
├── phonebook.py
└── README.md

---

Learning Concepts Demonstrated

This project helps practice:

- Python classes and methods
- Object instantiation
- Loop control
- List operations ("append", "delete", indexing)
- User interaction using "input()"
- Basic program flow control

---

Possible Improvements

Future improvements could include:

- Storing contacts in a file or database
- Allow editing of phone numbers
- Preventing duplicate contacts
- Adding contact validation
- Building a GUI version
- Using dictionaries instead of parallel lists

---

License

This project is open source and available for learning and educational purposes.
