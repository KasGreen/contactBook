# Contact Book

A command-line contact management application written in Python that stores contacts in a CSV file with support for adding, viewing, and deleting contacts.

## Features

- **Add Contacts**: Store contact information including name, email, and phone number
- **View Contacts**: Display all saved contacts in a formatted view
- **Delete Contacts**: Remove contacts by phone number
- **Persistent Storage**: Contacts are saved to a CSV file and persist between sessions
- **Auto-initialization**: Automatically creates the storage file on first run
- **Modular Design**: Separated into main application and editor package

## Installation

```bash
git clone https://github.com/KasGreen/contactBook.git
cd contactBook
```

## Usage

Run the contact book:

```bash
python contactBook.py
```

### Menu Options

```
Would you like to:
1: Add a new contact
2: Delete a contact
3: View all contacts
4: Exit the program
```

### Interactive Session Example

```
Would you like to:
1: Add a new contact
2: Delete a contact
3: View all contacts
4: Exit the program
1

What is the contacts first name?
John
What is the contacts last name?
Doe
What is the contacts email?
john.doe@email.com
What is the contacts phone number?
555-1234

Would you like to select another option y/n: y

Would you like to:
1: Add a new contact
2: Delete a contact
3: View all contacts
4: Exit the program
3

Name: John Doe
Email: john.doe@email.com
Number: 555-1234

Would you like to select another option y/n: n
Bye
```

## Project Structure

```
contactBook/
├── contactBook.py          # Main entry point
├── CBpackages/             # Contact Book packages
│   ├── __init__.py
│   └── CBeditor.py         # Core contact management functions
├── contacts.csv            # Data storage (auto-created)
├── LICENSE
└── .gitignore
```

## Contact Data Format

Contacts are stored in `contacts.csv` with the following structure:

| Field | Description |
|-------|-------------|
| First Name | Contact's first name |
| Last Name | Contact's last name |
| Email | Contact's email address |
| Phone Number | Contact's phone number (used as identifier for deletion) |

**CSV Format:**
```csv
John,Doe,john.doe@email.com,555-1234
Jane,Smith,jane.smith@email.com,555-5678
```

## API Reference

### Main Module (contactBook.py)

The entry point that provides the interactive menu interface.

| Function | Description |
|----------|-------------|
| `programExit()` | Prints farewell message and exits the program |

### CBeditor Module (CBpackages/CBeditor.py)

Core contact management functions.

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `createFileIfDosentExist()` | None | None | Creates `contacts.csv` if it doesn't exist |
| `addContact()` | None | None | Prompts for contact details and saves to file |
| `deleteContact()` | None | None | Prompts for phone number and removes matching contact |
| `viewContacts()` | None | None | Displays all contacts in formatted output |
| `isFileEmpty()` | None | bool | Returns `True` if contacts file is empty |

### Programmatic Usage

```python
from CBpackages import CBeditor as cbe

# Ensure storage file exists
cbe.createFileIfDosentExist()

# Add a contact (interactive)
cbe.addContact()

# View all contacts
cbe.viewContacts()

# Delete a contact (interactive - prompts for phone number)
cbe.deleteContact()

# Check if any contacts exist
if cbe.isFileEmpty():
    print("No contacts saved")
```

## Operations Detail

### Adding a Contact

1. Prompts for first name, last name, email, and phone number
2. Formats data as comma-separated values
3. Appends to `contacts.csv` (with newline if file not empty)

### Viewing Contacts

1. Checks if file has any data
2. Reads each line and parses CSV fields
3. Displays formatted output:
   ```
   Name: John Doe
   Email: john.doe@email.com
   Number: 555-1234
   ```

### Deleting a Contact

1. Prompts for phone number of contact to delete
2. Reads all contacts into memory
3. Filters out the matching contact
4. Rewrites the file without the deleted contact

## Error Handling

| Scenario | Behavior |
|----------|----------|
| File doesn't exist | Automatically created on startup |
| Empty contact list (view) | Displays "No contacts found" |
| Empty contact list (delete) | Displays "No contacts found" |
| Invalid menu option | Prompts "Please enter a valid number" |
| Non-numeric menu input | Prompts "Please enter a number" |
| Run as imported module | Exits with error message |
| Run CBeditor directly | Exits with error message |

## Module Protection

Both modules include protection against incorrect execution:

```python
# contactBook.py - Must be run as main
if __name__ != '__main__':
    print('Error: must be run as main module')
    sys.exit(1)

# CBeditor.py - Must NOT be run as main
if __name__ == '__main__':
    print('Error: can not be run as main module')
    sys.exit(1)
```

## Data Persistence

- Contacts are stored in `contacts.csv` in the same directory as the script
- File is automatically created if it doesn't exist
- Data persists between program runs
- CSV format allows easy viewing/editing with spreadsheet software

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

KasGreen

---

*Note: This is an educational project demonstrating file I/O operations, CSV handling, modular Python packaging, and command-line interface design.*
