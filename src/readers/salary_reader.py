import csv
import logging
from pathlib import Path


def load_salary(file_path: Path) -> list[dict[str, str]]:
    # Verify that the file exists
    if not file_path.exists():
        logging.error(f"Salary file not found: {file_path}")
        raise FileNotFoundError(f"Salary file not found: {file_path}")

    try:
        # Open the file
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            # Read CSV
            reader = csv.DictReader(file)
            salary_records = list(reader)

        # Return records
        return salary_records

    except Exception as e:
        logging.error(f"Failed to load salary data from {file_path}: {e}")
        raise


if __name__ == "__main__":
    salary_file = Path("data") / "python" / "salary.csv"
    salary = load_salary(salary_file)