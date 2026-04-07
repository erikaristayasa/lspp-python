import io
import math
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from app import part2


class TestPart2(unittest.TestCase):
    def test_get_positive_number_retries_until_valid(self) -> None:
        with patch("builtins.input", side_effect=["abc", "0", "-2", "4.5"]):
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                value = part2.get_positive_number("Masukkan angka: ")

        self.assertEqual(value, 4.5)
        output = buffer.getvalue()
        self.assertIn("Input harus berupa angka.", output)
        self.assertIn("Input harus lebih dari 0.", output)

    def test_select_shape_retries_until_valid_choice(self) -> None:
        with patch("builtins.input", side_effect=["9", "2"]):
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                selected = part2.select_shape()

        self.assertEqual(selected, "rectangle")
        self.assertIn("Pilihan shape tidak valid.", buffer.getvalue())

    def test_calculate_shape_result_square(self) -> None:
        with patch("app.part2.get_positive_number", return_value=4):
            area, perimeter = part2.calculate_shape_result("square")

        self.assertEqual(area, 16)
        self.assertEqual(perimeter, 16)

    def test_calculate_shape_result_rectangle(self) -> None:
        with patch("app.part2.get_positive_number", side_effect=[5, 3]):
            area, perimeter = part2.calculate_shape_result("rectangle")

        self.assertEqual(area, 15)
        self.assertEqual(perimeter, 16)

    def test_calculate_shape_result_circle(self) -> None:
        with patch("app.part2.get_positive_number", return_value=7):
            area, perimeter = part2.calculate_shape_result("circle")

        self.assertAlmostEqual(area, math.pi * 49)
        self.assertAlmostEqual(perimeter, math.pi * 14)

    def test_run_shape_calculator_prints_result(self) -> None:
        with patch("app.part2.select_shape", return_value="square"), patch(
            "app.part2.calculate_shape_result", return_value=(9, 12)
        ):
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                part2.run_shape_calculator()

        output = buffer.getvalue()
        self.assertIn("Shape dipilih: square", output)
        self.assertIn("Luas: 9.00", output)
        self.assertIn("Keliling: 12.00", output)


if __name__ == "__main__":
    unittest.main()
