import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "db" / "numbers.db"
SEED_DATA = [
	"dua",
	"empat",
	"delapan",
	"lima",
	"tujuh",
	"satu",
	"tiga",
	"enam",
	"sepuluh",
	"sembilan",
]

WORD_TO_NUMBER = {
	"satu": 1,
	"dua": 2,
	"tiga": 3,
	"empat": 4,
	"lima": 5,
	"enam": 6,
	"tujuh": 7,
	"delapan": 8,
	"sembilan": 9,
	"sepuluh": 10,
}


def initialize_table_and_records(connection: sqlite3.Connection) -> None:
	cursor = connection.cursor()
	cursor.execute("DROP TABLE IF EXISTS numbers")

	cursor.execute(
		"""
		CREATE TABLE numbers (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			angka INTEGER NOT NULL
		)
		"""
	)

	cursor.executemany(
		"INSERT INTO numbers (angka) VALUES (?)",
		[(WORD_TO_NUMBER[word],) for word in SEED_DATA],
	)
	connection.commit()


def display_records(connection: sqlite3.Connection) -> None:
	cursor = connection.cursor()
	cursor.execute("SELECT id, angka FROM numbers ORDER BY id")
	rows = cursor.fetchall()
	sorted_rows = sorted(rows, key=lambda row: row[1])

	headers = ["id", "angka", "label"]
	id_width = max(len(headers[0]), *(len(str(row[0])) for row in sorted_rows))
	angka_width = max(len(headers[1]), *(len(str(row[1])) for row in sorted_rows))
	labels = ["genap" if row[1] % 2 == 0 else "ganjil" for row in sorted_rows]
	label_width = max(len(headers[2]), *(len(label) for label in labels))

	border = f"+-{'-' * id_width}-+-{'-' * angka_width}-+-{'-' * label_width}-+"
	header_row = (
		f"| {headers[0].ljust(id_width)} | "
		f"{headers[1].ljust(angka_width)} | "
		f"{headers[2].ljust(label_width)} |"
	)

	print(border)
	print(header_row)
	print(border)

	for row, label in zip(sorted_rows, labels):
		print(
			f"| {str(row[0]).ljust(id_width)} | "
			f"{str(row[1]).ljust(angka_width)} | "
			f"{label.ljust(label_width)} |"
		)
		print(border)



def main() -> None:
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)

	with sqlite3.connect(DB_PATH) as connection:
		initialize_table_and_records(connection)
		display_records(connection)


if __name__ == "__main__":
	main()