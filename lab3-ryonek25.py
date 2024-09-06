import unittest
# Base Class
class Shape:
# Method 1
    def __init__(self, color="red"):
        self.color = color
# Method 2
    def get_color(self):
        return self.color

# Derived Class
class Rectangle(Shape):
# Method 1 
    def __init__(self, width, height, color="red"):
        super().__init__(color)
        self.width = width
        self.height = height
# Method 2 
    def area(self):
        return self.width * self.height

class TestRectangle(unittest.TestCase):
# Test Method 1
    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)
# Test Method 2
    def test_area_with_different_values(self):
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)

'''if __name__ == "__main__":
    unittest.main()'''

#Miles
#Nana Kwame



# Lab 3 
# Author: Ryan Yonek
# Date: 9/6/24

# Base class
class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        return "Dog sits"
    
# Derived class
class Terrier(Dog):
    def __init__(self, name, numSit):
        super().__init__(name)
        self.numSit = numSit

    def sit(self):
        return "Dog sits"

# Unit Tests
class Test(unittest.TestCase):

# Test for sit() method
    def test_sit(self):
        goodDog = Terrier("Dog sits", 10)
        self.assertEqual(goodDog.sit(), "Dog sits")

# Test for numSit() method
    def test_numSit(self):
        goodDog = Terrier("Dog sits", 10)
        self.assertEqual(goodDog.numSit, 10)

# Running all 4 tests
if __name__ == "__main__":
    unittest.main()


