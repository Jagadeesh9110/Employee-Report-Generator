from pathlib import Path
from typing import Any

from utils.csv_writer import write_csv_report


def generate_summary_report(
    records: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """
    Generate an organization summary report.

    Args:
        records: List of merged business records.
        output_path: Path where the report will be saved.
    """

    total_employees = len(records)

    active_employees = sum(
        1
        for record in records
        if record["status"] == "Active"
    )

    average_salary = (
        sum(record["net_salary"] for record in records)
        / total_employees
    )

    highest_salary = max(
        record["net_salary"] for record in records
    )

    lowest_salary = min(
        record["net_salary"] for record in records
    )

    average_attendance = (
        sum(
            record["attendance_percentage"]
            for record in records
        )
        / total_employees
    )

    total_overtime = sum(
        record["overtime_hours"]
        for record in records
    )

    rows = [
        {
            "total_employees": total_employees,
            "active_employees": active_employees,
            "average_salary": round(average_salary, 2),
            "highest_salary": highest_salary,
            "lowest_salary": lowest_salary,
            "average_attendance": round(average_attendance, 2),
            "total_overtime_hours": total_overtime,
        }
    ]

    fieldnames = [
        "total_employees",
        "active_employees",
        "average_salary",
        "highest_salary",
        "lowest_salary",
        "average_attendance",
        "total_overtime_hours",
    ]

    write_csv_report(
        rows=rows,
        fieldnames=fieldnames,
        output_path=output_path,
    )