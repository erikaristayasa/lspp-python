import part1
import part2


def select_part() -> str:
	while True:
		selected = input("Pilih bagian yang ingin dijalankan (1: bagian 1, 2: bagian 2): ").strip()
		if selected in {"1", "2"}:
			return selected

		print("Pilihan tidak valid. Masukkan 1 atau 2.")


def main() -> None:
	selected_part = select_part()

	if selected_part == "1":
		part1.main()
		return

	part2.run_shape_calculator()


if __name__ == "__main__":
	main()