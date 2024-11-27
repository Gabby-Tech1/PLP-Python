# Base class: Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class: Bird
class Bird(Animal):
    def move(self):
        print("Flying 🕊️")

# Derived class: Fish
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Derived class: Snake
class Snake(Animal):
    def move(self):
        print("Slithering 🐍")

# Demonstrate Polymorphism
animals = [Bird(), Fish(), Snake()]
for animal in animals:
    animal.move()
