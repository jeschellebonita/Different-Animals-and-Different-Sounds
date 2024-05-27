# Base class representing a generic animal with encapsulated attributes
class Animal:
    # Constructor to initialize the name attribute
    def __init__(self, name):
        self._name = name  # Encapsulation: '_name' is internal to this class

    # Method to retrieve the name (encapsulation)
    def get_name(self):
        return self._name

    # Abstract method for subclasses to implement their own behavior
    def speak(self):
        # Abstraction
        raise NotImplementedError("Subclasses must implement this method") 

# Derived class representing a dog, inheriting from Animal
class Dog(Animal):
    # Override the abstract 'speak' method to return a specific sound
    def speak(self):
        # Polymorphism
        return f"{self.get_name()} says Woof!"  

# Derived class representing a cat, inheriting from Animal
class Cat(Animal):
    # Override the abstract 'speak' method with a different implementation
    def speak(self):
        # Polymorphism
        return f"{self.get_name()} says Meow!"  

# Derived class representing a duck, inheriting from Animal
class Duck(Animal):
    # Override the abstract 'speak' method with yet another implementation
    def speak(self):
        # Polymorphism
        return f"{self.get_name()} says Quack!"  

# Function to demonstrate polymorphism by accepting an Animal instance
def animal_sound(animal):
    # Works with any class derived from Animal
    return animal.speak()  

# Create instances of Dog, Cat, and Duck
dog = Dog("Budoy")  
cat = Cat("Josep") 
duck = Duck("Danny") 

# Using polymorphism to get the sound of each animal
print(animal_sound(dog))  
print(animal_sound(cat)) 
print(animal_sound(duck))
