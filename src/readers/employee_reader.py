


import csv
import logging
from pathlib import Path



def load_employees(file_path: Path) -> list[dict[str,str]]:
    # Verify that the file exists
    if not file_path.exists():
        logging.error(f"Employee file not found: {file_path}")
        raise FileNotFoundError(f"Employee file not found: {file_path}")

    try:
        # open the file 
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            # Read csv
            reader = csv.DictReader(file)
            employees = list(reader)   
        # Return records
        return employees
    except Exception as e:
        logging.error(f"Failed to load employee data from {file_path}: {e}")
        raise # preserves the original exception type and traceback, which is very helpful for debugging.


if __name__ == "__main__":
    employee_file = Path("data") / "python" / "employees.csv"
    employees = load_employees(employee_file)