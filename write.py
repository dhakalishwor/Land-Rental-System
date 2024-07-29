LAND_REGISTRY_FILE = "land_registry.txt"

def update_land_registry(lands):
    with open(LAND_REGISTRY_FILE, 'w') as file:
        for land in lands:
            file.write(f"{land['kitta_number']}, {land['city_district']}, {land['direction']}, {land['area']}, {land['price']}, {land['availability']}\n")

