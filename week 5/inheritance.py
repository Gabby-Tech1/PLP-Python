# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"Device: {self.brand} {self.model}"

# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def details(self):
        return f"Smartphone: {self.brand} {self.model}, OS: {self.os}, Storage: {self.storage}GB"

    def make_call(self, number):
        print(f"Calling {number}...")

# Derived class: Tablet
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def details(self):
        return f"Tablet: {self.brand} {self.model}, Screen Size: {self.screen_size} inches"

# Create objects
phone = Smartphone("Apple", "iPhone 14", "iOS", 128)
tablet = Tablet("Samsung", "Galaxy Tab S8", 11)

# Print details
print(phone.details())
phone.make_call("123-456-7890")
print(tablet.details())
