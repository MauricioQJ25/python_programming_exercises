# Program to demonstrate how to create a class, init method, attributes

class Dog:
    # class attribute
    attr = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is: {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is {}".format(Rodger.__class__.attr))
print("Tommy is also a {}".format(Tommy.__class__.attr))

# Accesing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is{}".format(Tommy.name))

# Accesing speak method
Rodger.speak()
Tommy.speak()