import pandas as pd
import numpy as np

# --------------------------
# Custom Exception
# --------------------------
class LowSalaryException(Exception):
    def __init__(self, message="❌ Salary is too low. Showroom services not available."):
        super().__init__(message)


# --------------------------
# Car Class
# --------------------------
class Car:
    def __init__(self, brand, model, year, price, fuel, color):
        self.id = int(np.random.randint(1000, 9999))   # Unique Car ID
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.fuel = fuel
        self.color = color

    def get_details(self):
        return {
            "ID": self.id,
            "Brand": self.brand,
            "Model": self.model,
            "Year": self.year,
            "Price": self.price,
            "Fuel": self.fuel,
            "Color": self.color
        }


# --------------------------
# Showroom Class
# --------------------------
class Showroom:
    def __init__(self, name):
        self.name = name
        self.inventory = pd.DataFrame(columns=["ID", "Brand", "Model", "Year", "Price", "Fuel", "Color"])

    # Add Car to Inventory
    def buy_car(self, car: Car):
        car_data = car.get_details()
        self.inventory = pd.concat([self.inventory, pd.DataFrame([car_data])], ignore_index=True)
        print(f"✅ {car.brand} {car.model} added to inventory.")

    # View all cars
    def view_cars(self):
        if self.inventory.empty:
            print("❌ No cars available in the showroom.")
        else:
            print("\n🚗 Cars Available in Showroom:")
            print(self.inventory.to_string(index=False))

    # Display car details by ID
    def display_car(self, car_id):
        car = self.inventory[self.inventory["ID"] == car_id]
        if car.empty:
            print("❌ Car not found.")
        else:
            print("\n📌 Car Details:")
            print(car.to_string(index=False))

    # Sell car (remove from inventory)
    def sell_car(self, car_id):
        if car_id in self.inventory["ID"].values:
            car = self.inventory[self.inventory["ID"] == car_id]
            self.inventory = self.inventory[self.inventory["ID"] != car_id]
            print(f"✅ Sold Car: {car['Brand'].values[0]} {car['Model'].values[0]} (ID: {car_id})")
        else:
            print("❌ Car not found, cannot sell.")


# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    try:
        salary = float(input("Enter your monthly salary: "))

        # Raise custom exception if salary is too low
        if salary < 50000:
            raise LowSalaryException()

        showroom = Showroom("Super Cars")

        # Preload some cars
        car1 = Car("Tesla", "Model S", 2022, 80000, "Electric", "White")
        car2 = Car("BMW", "X5", 2021, 60000, "Diesel", "Black")
        car3 = Car("Toyota", "Corolla", 2020, 20000, "Petrol", "Blue")

        showroom.buy_car(car1)
        showroom.buy_car(car2)
        showroom.buy_car(car3)

        while True:
            print("\n===== Car Showroom Menu =====")
            print("1. View Available Cars")
            print("2. Display Car Details")
            print("3. Sell a Car")
            print("4. Buy a Car")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                showroom.view_cars()
            elif choice == "2":
                car_id = int(input("Enter Car ID to view details: "))
                showroom.display_car(car_id)
            elif choice == "3":
                car_id = int(input("Enter Car ID to sell: "))
                showroom.sell_car(car_id)
            elif choice == "4":
                brand = input("Enter Car Brand: ")
                model = input("Enter Car Model: ")
                year = int(input("Enter Car Year: "))
                price = float(input("Enter Car Price: "))
                fuel = input("Enter Fuel Type: ")
                color = input("Enter Car Color: ")

                new_car = Car(brand, model, year, price, fuel, color)
                showroom.buy_car(new_car)
            elif choice == "5":
                print("👋 Exiting Showroom System. Goodbye!")
                break
            else:
                print("❌ Invalid choice, please try again.")

    except LowSalaryException as e:
        print(e)
    except ValueError:
        print("❌ Invalid input! Please enter numeric values where required.")
