from pathlib import Path
from typing import Any

from utils.csv_writer import write_csv_report


def generate_employee_report(
    records: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """
    Generate an employee report.
    """

    fieldnames = [
        "employee_id",
        "employee_name",
        "department",
        "designation",
        "employment_type",
        "status",
        "joining_date",
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
                "department": record["department"],
                "designation": record["designation"],
                "employment_type": record["employment_type"],
                "status": record["status"],
                "joining_date": record["joining_date"],
            }
        )

    write_csv_report(
        rows=rows,
        fieldnames=fieldnames,
        output_path=output_path,
    )