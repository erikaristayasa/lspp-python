import io
import sqlite3
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import part1


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")

    def tearDown(self) -> None:
        self.connection.close()

    def test_initialize_table_and_records_creates_integer_table_and_seed_data(self) -> None:
        part1.initialize_table_and_records(self.connection)

        schema = self.connection.execute("PRAGMA table_info(numbers)").fetchall()
        self.assertEqual(schema[1][1], "angka")
        self.assertEqual(schema[1][2], "INTEGER")

        rows = self.connection.execute(
            "SELECT angka FROM numbers ORDER BY id"
        ).fetchall()
        values = [row[0] for row in rows]
        self.assertEqual(values, [2, 4, 8, 5, 7, 1, 3, 6, 10, 9])

    def test_update_numbers_records_deletes_ganjil_values(self) -> None:
        part1.initialize_table_and_records(self.connection)
        part1.update_numbers_records(self.connection)

        rows = self.connection.execute(
            "SELECT angka FROM numbers ORDER BY angka"
        ).fetchall()
        values = [row[0] for row in rows]
        self.assertEqual(values, [2, 4, 6, 8, 10])

    def test_display_records_outputs_sorted_rows_with_labels(self) -> None:
        part1.initialize_table_and_records(self.connection)

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            part1.display_records(self.connection)
        output = buffer.getvalue()

        self.assertIn("| id | angka | label", output)
        self.assertIn("ganjil", output)
        self.assertIn("genap", output)
        self.assertIn("| 6  | 1", output)
        self.assertIn("| 9  | 10", output)

    def test_main_creates_database_file_and_applies_update(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "numbers_test.db"

            with patch.object(part1, "DB_PATH", db_path):
                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    part1.main()

            self.assertTrue(db_path.exists())

            with sqlite3.connect(db_path) as conn:
                rows = conn.execute("SELECT angka FROM numbers ORDER BY angka").fetchall()
            values = [row[0] for row in rows]
            self.assertEqual(values, [2, 4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()
