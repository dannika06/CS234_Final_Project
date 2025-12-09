"""
A simple password strength checker that evaluates the strength
of a given password based on the presence of lowercase letters,
uppercase letters, digits, whitespaces, and special characters.
"""

import string
import getpass


def calculate_password_strength(
    password: str
) -> tuple[int, int, int, int, int]:
    """
    Calculates the strength of the given password by counting
    the occurrences of lowercase letters, uppercase letters,
    digits, whitespaces, and special characters.

    Args:
        password (str): The password to be evaluated.

    Returns:
        tuple: A tuple containing counts of lowercase letters,
            uppercase letters, digits, whitespaces,
            and special characters.
    """
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = (
        special_char_count
    ) = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == " ":
            whitespace_count += 1
        else:
            special_char_count += 1

    return (
        lower_alpha_count,
        upper_alpha_count,
        number_count,
        whitespace_count,
        special_char_count,
    )


def check_password_strength(password: str) -> None:
    """
    Checks the strength of the given password and prints the analysis.
    Args:
        password (str): The password to be checked.
    Returns:
        None
    """
    (
        lower_alpha_count,
        upper_alpha_count,
        number_count,
        whitespace_count,
        special_char_count,
    ) = calculate_password_strength(password)
    strength = 0
    remarks = ""

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "That's a very bad password. Change it as soon as possible."
    elif strength == 2:
        remarks = (
            "That's not a good password. Consider making a tougher password."
        )
    elif strength == 3:
        remarks = "Your password is okay, but it can be improved a lot"
    elif strength == 4:
        remarks = "Your password is hard to guess. Make it even more secure"
    elif strength == 5:
        remarks = (
            "That's one hell of a strong password!! "
            "Hackers will never guess it."
        )

    print("Your password has:-")
    print(f"{lower_alpha_count} lowercase letters")
    print(f"{upper_alpha_count} uppercase letters")
    print(f"{number_count} digits")
    print(f"{whitespace_count} whitespaces")
    print(f"{special_char_count} special characters")
    print(f"Password score: {strength}/5")
    print(f"Remarks: {remarks}")


print("===== Welcome to Password Strength Checker =====")
while 1:
    choice = input("Do you want to check a password's strength (y/n) : ")
    if "y" in choice.lower():
        user_password = getpass.getpass("Enter the password: ")
        check_password_strength(user_password)
    elif "n" in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...please try again.")
    print()
