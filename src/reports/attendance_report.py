from pathlib import Path
from typing import Any

from utils.csv_writer import write_csv_report


def generate_attendance_report(
    records: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """
    Generate an attendance report from merged business records.

    Args:
        records: List of merged business records.
        output_path: Path where the report will be saved.
    """

    fieldnames = [
        "employee_id",
        "employee_name",
        "month",
        "working_days",
        "present_days",
        "leave_days",
        "absent_days",
        "late_days",
        "attendance_percentage",
        "overtime_hours",
    ]

    rows = []

    for record in records:
        rows.append(
            {
                "employee_id": record["employee_id"],
                "employee_name": (
                    f"{record['first_name']} "
                    f"{record['last_name']}"
                ),
                "month": record["month"],
                "working_days": record["working_days"],
                "present_days": record["present_days"],
                "leave_days": record["leave_days"],
                "absent_days": record["absent_days"],
                "late_days": record["late_days"],
                "attendance_percentage": record["attendance_percentage"],
                "overtime_hours": record["overtime_hours"],
            }
        )

    write_csv_report(
        rows=rows,
        fieldnames=fieldnames,
        output_path=output_path,
    )