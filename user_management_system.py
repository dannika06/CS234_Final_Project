"""
A simple user management system that allows adding, updating, deleting,
searching, and displaying user entries.
"""
database = {"entries": []}

SRNO = "srno"
NAME = "name"
AGE = "age"
GENDER = "gender"
OCCUPATION = "occupation"


def get_serial_no() -> int:
    """
    Generates and returns the next serial number for a new entry.
    """
    return len(database["entries"]) + 1


def add_entry(entry: dict) -> None:
    """
    Adds a new entry to the database.
    Args:
        entry (dict): A dictionary containing entry details.
    Returns:
        None
    """
    entry = {
        "srno": get_serial_no(),
        "name": entry["name"],
        "age": entry["age"],
        "gender": entry["gender"],
        "occupation": entry["occupation"],
    }
    database["entries"].append(entry)


def check_entry_presence(value: tuple[str, str]) -> int:
    """
    Checks if an entry with the given value is present in the database.
    Args:
        value (tuple[str, str]): A tuple containing the key and value to check.
    Returns:
        int: 1 if the entry is present, 0 otherwise.
    """
    for entry in database["entries"]:
        if entry[value[0]] == value[1]:
            return 1
    return 0


def search_entry(value: tuple[str, str]) -> dict | None:
    """
    Searches for an entry with the given value in the database.
    Args:
        value (tuple[str, str]): A tuple containing the key and value to search for.
    Returns:
        dict | None: The entry if found, None otherwise.
    """
    for entry in database["entries"]:
        if entry[value[0]] == value[1]:
            return entry
    return None


def update_entry(value: tuple[str, str], updated_entry: dict) -> None:
    """
    Updates an existing entry in the database with new details.
    Args:
        value (tuple[str, str]): A tuple containing the key and value to identify the entry.
        updated_entry (dict): A dictionary containing the updated entry details.
    Returns:
        None
    """
    for num, entry in enumerate(database["entries"]):
        if entry[value[0]] == value[1]:
            database["entries"][num] = updated_entry


def delete_entry(value: tuple[str, str]) -> None:
    """
    Deletes an entry with the given value from the database.
    Args:
        value (tuple[str, str]): A tuple containing the key and value to identify the entry.
    Returns:
        None
    """
    for entry in database["entries"]:
        if entry[value[0]] == value[1]:
            database["entries"].remove(entry)


def display_entry(entry: dict[str, str] | None) -> None:
    """
    Displays the details of a single entry.
    Args:
        entry (dict[str, str] | None): The entry to display.
    Returns:
        None
    """
    if entry is None:
        print("Entry not found.")
        return
    print(f"SRNO: {entry['srno']}")
    print(f"Name: {entry['name']}")
    print(f"Age: {entry['age']}")
    print(f"Gender: {entry['gender']}")
    print(f"Occupation: {entry['occupation']}\n")


def display_all_entries() -> None:
    """
    Displays all entries in the database.
    Returns:
        None
    """
    for entry in database["entries"]:
        display_entry(entry)


def select_entry_and_value() -> tuple[str, str]:
    """
    Prompts the user to select an entry and value type for searching.
    Returns:
        tuple[str, str]: A tuple containing the selected entry type and value.
    """
    value_type = ""
    value = ""
    while 1:
        print("Choose an entry based on which to search entries in database: ")
        print("1. srno")
        print("2. name")
        print("3. age")
        print("4. gender")
        print("5. occupation")
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            print("Invalid input...please try again")
        else:
            if choice == 1:
                value_type = SRNO
                value = input("Enter serial number to search: ")
                return (value_type, value)
            if choice == 2:
                value_type = NAME
                value = input("Enter name to search: ")
                return (value_type, value)
            if choice == 3:
                value_type = AGE
                value = input("Enter age to search: ")
                return (value_type, value)
            if choice == 4:
                value_type = GENDER
                value = input("Enter gender to search: ")
                return (value_type, value)
            if choice == 5:
                value_type = OCCUPATION
                value = input("Enter occupation to search: ")
                return (value_type, value)
    return "", ""


def get_entry_details() -> dict[str, str]:
    """
    Prompts the user to enter details for a new entry.
    Returns:
        dict[str, str]: A dictionary containing the details of the new entry.
    """
    output = {}
    output[NAME] = input("Enter name: ")
    output[AGE] = input("Enter age: ")
    output[GENDER] = input("Enter gender: ")
    output[OCCUPATION] = input("Enter occupation: ")
    return output


print("===== Welcome To User Management System =====")
while 1:
    print("\nWhat would you like to do:-")
    print("1. Add an entry")
    print("2. Update an entry")
    print("3. Delete an entry")
    print("4. Search an entry")
    print("5. Display all entries")
    print("6. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice > 7 or user_choice < 1:
        print("Invalid input...please try again")
    else:
        if user_choice == 1:
            print("Enter details for the new entry:-")
            user_entry = get_entry_details()
            add_entry(user_entry)
            print("Entry successfully created...")
        elif user_choice == 2:
            user_value = select_entry_and_value()
            print("Enter the details of the updated entry:-")
            user_entry = get_entry_details()
            update_entry(user_value, user_entry)
            print("Entry successfully updated...")
        elif user_choice == 3:
            user_value = select_entry_and_value()
            delete_entry(user_value)
            print("Entry successfully deleted...")
        elif user_choice == 4:
            user_value = select_entry_and_value()
            user_entry = search_entry(user_value)
            display_entry(user_entry)
        elif user_choice == 5:
            display_all_entries()
        elif user_choice == 6:
            print("Exiting")
            break
