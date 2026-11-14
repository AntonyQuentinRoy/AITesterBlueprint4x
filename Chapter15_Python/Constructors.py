class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def print_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

hyundai = Car("Hyundai", "Creta", 1500000)
hyundai.print_details()
honda = Car("Honda", "City", 2000000)
honda.print_details()
maruti = Car("Maruti", "Swift", 800000)
maruti.print_details()