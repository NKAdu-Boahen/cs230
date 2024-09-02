import unittest
import random

class Shape:
    def __init__(self, color="red"):
        self.color = color

    def get_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, width, height, color="red"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def get_random_fact(self):
        facts = [
            "Rectangles have four right angles.",
            "The area of a rectangle is width times height.",
            "A square is a special case of a rectangle.",
            "The perimeter of a rectangle is twice the sum of its width and height.",
            "In 2D space, rectangles are everywhere!"
        ]
        return random.choice(facts)

    def describe_rectangle(self):
        return f"A {self.color} rectangle with width {self.width} and height {self.height}."

class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_area_with_different_values(self):
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)

    def test_random_fact(self):
        rect = Rectangle(3, 9)
        fact = rect.get_random_fact()
        self.assertIn(fact, [
            "Rectangles have four right angles.",
            "The area of a rectangle is width times height.",
            "A square is a special case of a rectangle.",
            "The perimeter of a rectangle is twice the sum of its width and height.",
            "In 2D space, rectangles are everywhere!"
        ])

    def test_describe_rectangle(self):
        rect = Rectangle(4, 5, color="blue")
        description = rect.describe_rectangle()
        self.assertEqual(description, "A blue rectangle with width 4 and height 5.")

if __name__ == "__main__":
    unittest.main()
#Selormseditgit 
#Miles
#Nana Kwame
