import csv
import logging
from pathlib import Path


def load_attendance(file_path: Path) -> list[dict[str, str]]:
    # Verify that the file exists
    if not file_path.exists():
        logging.error(f"Attendance file not found: {file_path}")
        raise FileNotFoundError(f"Attendance file not found: {file_path}")

    try:
        # Open the file
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            # Read CSV
            reader = csv.DictReader(file)
            attendance_records = list(reader)

        # Return records
        return attendance_records

    except Exception as e:
        logging.error(f"Failed to load attendance data from {file_path}: {e}")
        raise


if __name__ == "__main__":
    attendance_file = Path("data") / "python" / "attendance.csv"
    attendance = load_attendance(attendance_file)