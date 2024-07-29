

LAND_REGISTRY_FILE = "land_registry.txt"

def display_available_lands():
    lands = load_land_registry()
    print("Available Lands:")
    for land in lands:
        if land['availability'] == "Available":
            print("|---------------------------------------------------------------------------------------------------------------------|")
            print(f"  Kitta Number: {land['kitta_number']}, Location: {land['city_district']}, Area: {land['area']} anna, Price: {land['price']} NPR")
            print("|---------------------------------------------------------------------------------------------------------------------|")



def display_unavailable_lands():
    lands = load_land_registry()
    print("Unavailable Lands:")
    for land in lands:
        if land['availability'] == "Not Available":
            print("|---------------------------------------------------------------------------------------------------------------------|")
            print(f"  Kitta Number: {land['kitta_number']}, Location: {land['city_district']}, Area: {land['area']} anna, Price: {land['price']} NPR")
            print("|---------------------------------------------------------------------------------------------------------------------|")



def load_land_registry():
    lands = []
    with open(LAND_REGISTRY_FILE, 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            land = {
                "kitta_number": int(data[0]),    # kitta number
                "city_district": data[1],        # city/district
                "direction": data[2],            # direction of the land
                "area": int(data[3]),            # area of land (anna)
                "price": int(data[4]),           # price in Nepalese Rupee
                "availability": data[5]          # availability status
            }
            lands.append(land)
    return lands

