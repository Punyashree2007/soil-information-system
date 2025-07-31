class Soil:
    def __init__(self, name, nitrogen, phosphorus, potassium, ph, crops, regions):
        self.name = name
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.ph = ph
        self.crops = crops
        self.regions = regions

    def get_details(self):
        details = (
            f"\nSoil Type: {self.name}\n"
            f"Nitrogen: {self.nitrogen}\n"
            f"Phosphorus: {self.phosphorus}\n"
            f"Potassium: {self.potassium}\n"
            f"pH Range: {self.ph}\n"
            f"Suitable Crops: {', '.join(self.crops)}\n"
            f"Common Regions: {', '.join(self.regions)}\n"
        )
        return details

    def show_details(self):
        print(self.get_details())


class SoilSystem:
    def __init__(self):
        self.soils = []
        self.add_soils()

    def add_soils(self):
        self.soils.append(Soil("Alluvial", "Moderate", "Low", "High", "6.5 - 8.4",
            ["Rice", "Wheat", "Sugarcane", "Maize", "Pulses", "Vegetables"],
            ["Northern Plains", "Bihar", "Punjab", "Uttar Pradesh","Karnataka"]))

        self.soils.append(Soil("Black", "Low", "Moderate", "High", "7.5 - 8.5",
            ["Cotton", "Soybean", "Sorghum", "Millets", "Sunflower", "Pulses"],
            ["Deccan Plateau", "Maharashtra", "Madhya Pradesh", "Gujarat", "Andhra Pradesh"]))

        self.soils.append(Soil("Red", "Low", "Low", "Moderate", "5.5 - 7",
            ["Millets", "Groundnut", "Potato", "Oilseeds", "Pulses"],
            ["Tamil Nadu", "Chhattisgarh", "Odisha", "Karnataka", "Andhra Pradesh"]))

        self.soils.append(Soil("Laterite", "Very Low", "Low", "Moderate", "4.5 - 6",
            ["Tea", "Coffee", "Cashew", "Rubber", "Pineapple"],
            ["Kerala", "Assam", "Karnataka", "Western Ghats", "Meghalaya"]))

        self.soils.append(Soil("Desert", "Very Low", "Very Low", "Low", "8.0+",
            ["Barley", "Millets", "Cactus", "Dates"],
            ["Rajasthan", "Northwestern India", "Thar Desert", "Jaisalmer"]))

        self.soils.append(Soil("Mountain", "Low", "Moderate", "Low", "4.5 - 6.5",
            ["Tea", "Spices", "Apples", "Barley"],
            ["Himachal Pradesh", "Uttarakhand", "Sikkim", "Darjeeling", "Nagaland"]))

        self.soils.append(Soil("Peaty and Marshy", "High", "High", "Low", "5.5 - 6.5",
            ["Paddy", "Vegetables", "Jute"],
            ["Kottayam", "Sundarbans", "Alappuzha", "West Bengal", "Odisha"]))

    def save_to_file(self, data):
        with open("soil_output.txt", "a") as file:
            file.write(data)
            file.write("-" * 40 + "\n")
        print("✔️ Soil details saved to 'soil_output.txt'.")

    def ask_save(self, data):
        choice = input("Do you want to save this information to a file? (y/n): ").lower()
        if choice == 'y':
            self.save_to_file(data)

    def show_soil_by_name(self):
        name = input("Enter soil type name: ").lower()
        found = False
        for soil in self.soils:
            if soil.name.lower() == name:
                details = soil.get_details()
                print(details)
                self.ask_save(details)
                found = True
        if not found:
            print("Soil not found. Try names like Alluvial, Black, Red, etc.")

    def find_by_crop(self):
        crop = input("Enter crop name: ").lower()
        found = False
        for soil in self.soils:
            if crop in [c.lower() for c in soil.crops]:
                details = soil.get_details()
                print(details)
                self.ask_save(details)
                found = True
        if not found:
            print("No soil found for that crop.")

    def find_by_region(self):
        region = input("Enter region: ").lower()
        found = False
        for soil in self.soils:
            if region in [r.lower() for r in soil.regions]:
                details = soil.get_details()
                print(details)
                self.ask_save(details)
                found = True
        if not found:
            print("No soil found in that region.")

    def menu(self):
        while True:
            print("\n--- Soil Info System ---")
            print("1. Know about a soil")
            print("2. Find soil for a crop")
            print("3. Find soil in a region")
            print("4. Exit")
            choice = input("Choose (1-4): ")

            if choice == '1':
                self.show_soil_by_name()
            elif choice == '2':
                self.find_by_crop()
            elif choice == '3':
                self.find_by_region()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid input. Choose 1 to 4.")


if __name__ == "__main__":
    system = SoilSystem()
    system.menu()
