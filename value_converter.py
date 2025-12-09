"""
A simple value converter that can convert temperature, currency and lengths.
"""

import sys


def convert_temperature() -> None:
    """
     Converts temperature between Celsius and Faranheit based on user choice.
     """
    print("\nWhich conversion do you want to choose:-")
    print("1. Celsius to Faranheit")
    print("2. Faranheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter temperature in celsius: "))
        print(f"{temp} degree celsius is equal to {(temp*9/5)+32} degree faranheit.\n")
    elif choice == 2:
        temp = float(input("Enter temperature in faranheit: "))
        print(f"{temp} degree faranheit is equal to {(temp-32)*5/9} degree celsius.\n")
    else:
        print("Invalid input...please try again\n")


def convert_currency() -> None:
    """
    Converts currency between Dollar and Pound based on user choice.
    """
    print("\nWhich conversion do you want to choose:-")
    print("1. Dollar to pound")
    print("2. Pound to Dollar")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter currency in dollars: "))
        print(f"{value} dollars in pounds will be {value*0.73}\n")
    elif choice == 2:
        value = float(input("Enter currency in pounds: "))
        print(f"{value} pounds in dollars will be {value/0.73}\n")


def convert_lengths() -> None:
    """
    Converts lengths between Centimeters and Foot/Inches based on user choice.
    """
    print("\nWhich conversion do you want to choose:-")
    print("1. Centimeters to foot and inches")
    print("2. Foot and inches to centimeter")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter length in cm: "))
        inches = value / 2.54
        feet = inches / 12
        print(f"{value} centimeters in equal to {feet} feet and {inches} inch\n")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        inches = float(input("Enter length in inches: "))
        length = (feet * 12 + inches) * 2.54
        print(f"{feet} feet and {inches} inches in centimeters will be {length}\n")


print("===== Welcome to Value Converter =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        convert_temperature()
    elif user_choice == 2:
        convert_currency()
    elif user_choice == 3:
        convert_lengths()
    elif user_choice == 4:
        print("Exiting...")
        sys.exit(0)
