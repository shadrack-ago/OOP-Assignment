# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def show_info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Inheritance example (Encapsulation + Layer)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_mp):
        super().__init__(brand, model, storage)
        self.__camera_mp = camera_mp  # encapsulated (private)

    def show_camera(self):
        print(f"Camera Quality: {self.__camera_mp} MP")

# Create objects
phone1 = AdvancedSmartphone("Samsung", "Galaxy S22", 256, 108)
phone2 = AdvancedSmartphone("Apple", "iPhone 14", 128, 48)

# Use methods
phone1.show_info()
phone1.show_camera()
