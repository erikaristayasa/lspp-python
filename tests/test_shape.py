import sys
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from models.shape import Circle, Rectangle, Shape, Square


class TestShapeModels(unittest.TestCase):
    def test_shape_base_methods_return_none(self) -> None:
        self.assertIsNone(Shape.calculateArea())
        self.assertIsNone(Shape.calculatePerimeter())

    def test_rectangle_initialization(self) -> None:
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 3)

    def test_circle_initialization(self) -> None:
        circle = Circle(7)
        self.assertEqual(circle.radius, 7)

    def test_square_side_assignment_and_custom_initializer_method(self) -> None:
        square = Square()
        square.__int__(4)
        self.assertEqual(square.side, 4)


if __name__ == "__main__":
    unittest.main()
