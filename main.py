# main.py

from operation import rent_land, return_land
from read import load_land_registry , display_available_lands , display_unavailable_lands

def main():
    while True:
        print("------------------------------------")
        print("Welcome to the Techno Property Nepal")
        print("------------------------------------")
        print("___________________________________")
        print("|Here the available choice for you|")
        print("|---------------------------------|")
        print("|1. Display Available Lands       |")
        print("|---------------------------------|")
        print("|2. Display UnAvailable Lands     |")
        print("|---------------------------------|")
        print("|3. Rent Land                     |")
        print("|---------------------------------|")
        print("|4. Return Land                   |")
        print("|---------------------------------|")
        print("|5. Exit                          |")
        print("+---------------------------------+")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_available_lands()
        elif choice == "2":
            display_unavailable_lands()
        elif choice == "3":
            display_available_lands()
            rent_land()
        elif choice == "4":
            display_unavailable_lands()
            return_land()
        elif choice == "5":
            print("____________________________")
            print("|--------------------------|")
            print("| Thanks for choosing Us!! |")
            print("|..........................|")
            print("+--------------------------+")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
