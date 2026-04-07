import math

from models.shape import Circle, Rectangle, Square


def get_positive_number(prompt: str) -> float:
	while True:
		raw_value = input(prompt).strip()
		try:
			value = float(raw_value)
		except ValueError:
			print("Input harus berupa angka.")
			continue

		if value <= 0:
			print("Input harus lebih dari 0.")
			continue

		return value


def select_shape() -> str:
	shape_aliases = {
		"1": "square",
		"2": "rectangle",
		"3": "circle",
	}

	while True:
		selected = input("Pilih shape (1:square, 2:rectangle, 3:cirlce): ").strip().lower()
		normalized = shape_aliases.get(selected)
		if normalized:
			return normalized

		print("Pilihan shape tidak valid.")


def calculate_shape_result(shape_name: str) -> tuple[float, float]:
	if shape_name == "square":
		side = get_positive_number("Masukkan panjang sisi: ")
		square = Square()
		square.side = side
		area = square.side * square.side
		perimeter = 4 * square.side
		return area, perimeter

	if shape_name == "rectangle":
		length = get_positive_number("Masukkan panjang: ")
		width = get_positive_number("Masukkan lebar: ")
		rectangle = Rectangle(length, width)
		area = rectangle.length * rectangle.width
		perimeter = 2 * (rectangle.length + rectangle.width)
		return area, perimeter

	radius = get_positive_number("Masukkan radius: ")
	circle = Circle(radius)
	area = math.pi * circle.radius * circle.radius
	perimeter = 2 * math.pi * circle.radius
	return area, perimeter


def run_shape_calculator() -> None:
	shape_name = select_shape()
	area, perimeter = calculate_shape_result(shape_name)

	print(f"Shape dipilih: {shape_name}")
	print(f"Luas: {area:.2f}")
	print(f"Keliling: {perimeter:.2f}")


if __name__ == "__main__":
	run_shape_calculator()
