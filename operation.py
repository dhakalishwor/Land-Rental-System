from read import load_land_registry
from write import update_land_registry

# opration for renting lands
def take_customer_name():
    while True:
        try:
            customer_name = input("Enter your name: ").strip()
            if not customer_name:
                raise ValueError("Name cannot be empty.")
        except ValueError as ve:
            print(ve)
        else:
            return customer_name

def take_customer_number():
    while True:
        customer_number = input("Enter your phone number: ").strip()
        if not customer_number:
            print("Phone number cannot be empty.")
        else:
            return customer_number

def take_customer_address():
    while True:
        customer_address = input("Enter your address: ").strip()
        if not customer_address:
            print("Address cannot be empty.")
        else:
            return customer_address


def take_kitta_number():
    while True:
        try:
            kitta_number = int(input("Enter the kitta number of the land to rent: "))
            if kitta_number < 0:
                print("Please enter a positive kitta number.")
            else:
                return kitta_number
        except ValueError:
            print("Invalid input. Please enter a valid kitta number.")


def take_rent_duration():
    while True:
        try:
            duration_months = int(input("Enter duration (in months) for rent: "))
            if duration_months > 0:
                return duration_months
            else:
                print("Please enter a valid positive number for duration.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# function of rent lands
def rent_land():
    customer_name = take_customer_name()
    customer_address = take_customer_address()
    customer_number = take_customer_number()
    kitta_number = take_kitta_number()
    rent_duration = take_rent_duration()

    lands = load_land_registry()
    total_amount = 0

    for land in lands:
        if land['kitta_number'] == kitta_number and land['availability'] == "Available":
            total_amount += rent_duration * land['price']
            land['availability'] = "Not Available"

    update_land_registry(lands)
    
    if total_amount > 0:
        print("Rent successful. Invoice generated.")
        generate_rent_invoice(customer_name, kitta_number, customer_address,customer_number, rent_duration, total_amount)
        
    else:
        print(f"No available land found with the provided kitta number: {kitta_number}.")

def generate_rent_invoice(customer_name, kitta_number,customer_address,customer_number, rent_duration, total_amount):
    invoice_file_name = f"{customer_name}_invoices.txt"
    rent_invoice_content = (
        "______________________________________________\n"
        "            Techno Property Nepal            \n"
        "---------------------------------------------\n"
        f"Customer Name: {customer_name}\n"
        f"Customer Address:{customer_address}\n"
        f"Contact Number:{customer_number}\n"
        "---------------------------------------------\n"
        f"Kitta Number: {kitta_number}\n"
        f"Rent Duration: {rent_duration} months  \n"
        "---------------------------------------------\n"
        "---------------------------------------------\n"
        f"Total Amount: {total_amount} NPR   \n"
        "---------------------------------------------\n"
    )

    with open(invoice_file_name, 'a') as invoice_file:
        invoice_file.write(rent_invoice_content)

    print(rent_invoice_content)
    return invoice_file_name

# For Returning the lands
def return_kitta_number():
    while True:
        try:
            kitta_number = int(input("Enter the kitta number of the land to return: "))
            if kitta_number < 0:
                print("Please enter a positive kitta number.")
            else:
                return kitta_number
        except ValueError:
            print("Invalid input. Please enter a valid kitta number.")


def take_return_duration():
    while True:
        try:
            duration_months = int(input("Enter duration (in months) for return: "))
            if duration_months > 0:
                return duration_months
            else:
                print("Please enter a valid positive number for duration.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def return_land():
    try:
        customer_name = take_customer_name()
        customer_address = take_customer_address()
        customer_number = take_customer_number()
        kitta_number = return_kitta_number()
        rent_duration_months = take_rent_duration()
        return_duration = take_return_duration()

        inventory = load_land_registry()
        returned_land = None

        for land in inventory:
            if land['kitta_number'] == kitta_number and land['availability'] == "Not Available":
                returned_land = land
                break
        
        if returned_land:
            returned_land['availability'] = "Available"

            rent_price_per_month = returned_land['price']
            total_amount_due = rent_price_per_month * rent_duration_months

            rent_duration = rent_duration_months
            late_months = return_duration - rent_duration

            if late_months >= 0:
                fine_rate_per_month = 10000  # Example: NPR 10000 fine per month of delay
                fine_amount = fine_rate_per_month * late_months
                total_amount_due += fine_amount

            # Print invoice to terminal
            print("_______________________________________________")
            print("            Techno Property Nepal            ")
            print("------------------------------------------------")
            print(f"Customer Name: {customer_name}")
            print(f"Contact Number: {customer_number}")
            print(f"Customer Address: {customer_address}")
            print("------------------------------------------------")
            print(f"Kitta Number: {returned_land['kitta_number']}")
            print(f"City/District: {returned_land['city_district']}")
            print(f"Area: {returned_land['area']} anna")
            print("------------------------------------------------")
            print(f"Rented for: {rent_duration_months} months")
            print(f"Returned After: {return_duration} months")
            print("------------------------------------------------")
            print(f"Fine: {fine_amount} NPR")
            print("------------------------------------------------")
            print(f"Total Amount with fine: {total_amount_due} NPR")
            print("------------------------------------------------")

            # Write invoice to file
            return_invoice_file = f"invoice_return_{customer_name}.txt"
            with open(return_invoice_file, 'a') as invoice:
                invoice.write("_______________________________________________\n")
                invoice.write("            Techno Property Nepal            \n")
                invoice.write("------------------------------------------------\n")
                invoice.write(f"Customer Name: {customer_name}\n")
                invoice.write(f"Address: {customer_address}\n")
                invoice.write(f"Contact Number: {customer_number}\n")
                invoice.write("------------------------------------------------\n")
                invoice.write(f"Kitta Number: {returned_land['kitta_number']}\n")
                invoice.write(f"City/District: {returned_land['city_district']}\n")
                invoice.write(f"Area: {returned_land['area']} anna\n")
                invoice.write("------------------------------------------------\n")
                invoice.write(f"Rented for: {rent_duration_months} months\n")
                invoice.write(f"Returned After: {return_duration} months\n")
                invoice.write("------------------------------------------------\n")
                invoice.write(f"Fine: {fine_amount} NPR\n")
                invoice.write("------------------------------------------------\n")
                invoice.write(f"Total Amount with fine: {total_amount_due} NPR\n")
                invoice.write("------------------------------------------------\n")

            
            update_land_registry(inventory)
            print(f"Return successful. Return invoice generated: {return_invoice_file}")
            
        else:
            print("No rented land found matching the provided kitta number.")
    except Exception as e:
        print(f"An error occurred: {e}")



