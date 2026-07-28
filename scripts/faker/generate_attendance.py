"""
Generate attendance dataset from employees.csv.

Output:
    data/faker/attendance.csv
"""

import csv
import random
import calendar
from pathlib import Path
from datetime import datetime

CSV_HEADER = [
        "attendance_id",
        "employee_id",
        "month",
        "working_days",
        "present_days",
        "leave_days",
        "absent_days",
        "late_days",
        "expected_working_hours",
        "actual_working_hours",
        "overtime_hours",
        "attendance_percentage",
]



def get_working_days(year, month):
    """
    Calculate actual Monday-Friday working days
    for a given month.
    """
    _, total_days = calendar.monthrange(year, month)

    return sum(
        1
        for day in range(1, total_days + 1)
        if datetime(year, month, day).weekday() < 5
    )


def generate_data():

    YEAR = 2025

    BASE_DIR = Path(__file__).resolve().parents[2]

    EMPLOYEE_FILE = BASE_DIR / "data" / "faker" / "employees.csv"
    OUTPUT_FILE = BASE_DIR / "data" / "faker" / "attendance.csv"

    attendance = []
    attendance_id = 1

    with open(EMPLOYEE_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for employee in reader:

            # Convert joining date string into datetime object
            joining_date = datetime.strptime(
                employee["joining_date"],
                "%Y-%m-%d",
            )

            joining_year = joining_date.year
            joining_month = joining_date.month

            # Ignore employees joining after 2025
            if joining_year > YEAR:
                continue

            # Generate attendance only for valid months
            for month in range(1, 13):

                # Skip months before the joining month
                if joining_year == YEAR and month < joining_month:
                    continue

                # Calculate actual weekdays (Monday-Friday)
                working_days = get_working_days(YEAR, month)

                # Select attendance category
                attendance_bucket = random.choices(
                    ["excellent", "good", "average", "poor"],
                    weights=[60, 25, 10, 5],
                    k=1,
                )[0]

                # Generate present days based on category
                if attendance_bucket == "excellent":
                    present_days = random.randint(
                        working_days - 1,
                        working_days,
                    )
                elif attendance_bucket == "good":
                    present_days = random.randint(
                        working_days - 3,
                        working_days - 1,
                    )
                elif attendance_bucket == "average":
                    present_days = random.randint(
                        working_days - 5,
                        working_days - 3,
                    )
                else:
                    present_days = random.randint(
                        max(working_days - 7, 0),
                        working_days - 5,
                    )

                # Remaining days become leave/absence
                remaining_days = working_days - present_days

                leave_days = random.randint(
                    0,
                    remaining_days,
                )

                absent_days = remaining_days - leave_days

                # Better attendance usually means fewer late arrivals
                if present_days >= working_days - 1:
                    late_days = random.randint(0, 2)
                elif present_days >= working_days - 3:
                    late_days = random.randint(1, 3)
                else:
                    late_days = random.randint(2, 5)

                # Expected monthly working hours
                expected_working_hours = working_days * 8

                # Decide overtime pattern
                overtime_bucket = random.choices(
                    ["none", "low", "high"],
                    weights=[70, 20, 10],
                    k=1,
                )[0]

                if overtime_bucket == "none":
                    overtime_hours = 0
                elif overtime_bucket == "low":
                    overtime_hours = random.randint(1, 4)
                else:
                    overtime_hours = random.randint(5, 12)

                # Small variation in actual worked hours
                hour_adjustment = random.randint(-4, 2)

                actual_working_hours = (
                    present_days * 8
                    + hour_adjustment
                    + overtime_hours
                )

                # Prevent negative hours
                actual_working_hours = max(
                    actual_working_hours,
                    0,
                )

                # Attendance percentage
                attendance_percentage = round(
                    (present_days / working_days) * 100,
                    2,
                )

                # Store attendance record
                attendance.append([
                    attendance_id,
                    employee["employee_id"],
                    f"{YEAR}-{month:02d}",
                    working_days,
                    present_days,
                    leave_days,
                    absent_days,
                    late_days,
                    expected_working_hours,
                    actual_working_hours,
                    overtime_hours,
                    attendance_percentage,
                ])

                attendance_id += 1

    # Write attendance dataset to CSV
    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.writer(file)

        writer.writerow(CSV_HEADER)
        writer.writerows(attendance)

    print(f"Generated {len(attendance)} attendance records.")
    print(f"Output File: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_data()
