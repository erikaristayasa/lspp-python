import sys
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from models.shape import Circle, Rectangle, Shape, Square


class TestShapeModels(unittest.TestCase):
    def test_shape_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Shape()

    def test_rectangle_initialization(self) -> None:
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 3)

    def test_circle_initialization(self) -> None:
        circle = Circle(7)
        self.assertEqual(circle.radius, 7)

    def test_square_initialization(self) -> None:
        square = Square(4)
        self.assertEqual(square.side, 4)

    def test_polymorphic_area_and_perimeter_calls(self) -> None:
        shapes = [Square(4), Rectangle(5, 3), Circle(7)]

        areas = [shape.calculateArea() for shape in shapes]
        perimeters = [shape.calculatePerimeter() for shape in shapes]

        self.assertEqual(areas[0], 16)
        self.assertEqual(perimeters[0], 16)
        self.assertEqual(areas[1], 15)
        self.assertEqual(perimeters[1], 16)
        self.assertAlmostEqual(areas[2], 153.93804002589985)
        self.assertAlmostEqual(perimeters[2], 43.982297150257104)


if __name__ == "__main__":
    unittest.main()
