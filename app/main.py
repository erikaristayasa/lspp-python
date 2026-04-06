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


def initialize_table_and_records(connection: sqlite3.Connection) -> None:
	cursor = connection.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS numbers (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			angka TEXT NOT NULL
		)
		"""
	)

	cursor.execute("DELETE FROM numbers")
	cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'numbers'")
	cursor.executemany(
		"INSERT INTO numbers (angka) VALUES (?)",
		[(value,) for value in SEED_DATA],
	)
	connection.commit()


def display_records(connection: sqlite3.Connection) -> None:
	cursor = connection.cursor()
	cursor.execute("SELECT id, angka FROM numbers ORDER BY id")
	rows = cursor.fetchall()

	headers = ["id", "angka"]
	id_width = max(len(headers[0]), *(len(str(row[0])) for row in rows))
	angka_width = max(len(headers[1]), *(len(str(row[1])) for row in rows))

	border = f"+-{'-' * id_width}-+-{'-' * angka_width}-+"
	header_row = f"| {headers[0].ljust(id_width)} | {headers[1].ljust(angka_width)} |"

	print(border)
	print(header_row)
	print(border)

	for row in rows:
		print(f"| {str(row[0]).ljust(id_width)} | {str(row[1]).ljust(angka_width)} |")
		print(border)



def main() -> None:
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)

	with sqlite3.connect(DB_PATH) as connection:
		initialize_table_and_records(connection)
		display_records(connection)


if __name__ == "__main__":
	main()