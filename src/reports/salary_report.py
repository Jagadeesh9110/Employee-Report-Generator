from pathlib import Path
from typing import Any

from utils.csv_writer import write_csv_report


def generate_salary_report(
    records: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """
    Generate a salary report from merged business records.

    Args:
        records: List of merged business records.
        output_path: Path where the report will be saved.
    """

    fieldnames = [
        "employee_id",
        "employee_name",
        "month",
        "basic_salary",
        "hra",
        "special_allowance",
        "overtime_pay",
        "gross_salary",
        "tax_deduction",
        "pf_deduction",
        "leave_deduction",
        "total_deductions",
        "net_salary",
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
                "basic_salary": record["basic_salary"],
                "hra": record["hra"],
                "special_allowance": record["special_allowance"],
                "overtime_pay": record["overtime_pay"],
                "gross_salary": record["gross_salary"],
                "tax_deduction": record["tax_deduction"],
                "pf_deduction": record["pf_deduction"],
                "leave_deduction": record["leave_deduction"],
                "total_deductions": record["total_deductions"],
                "net_salary": record["net_salary"],
            }
        )

    write_csv_report(
        rows=rows,
        fieldnames=fieldnames,
        output_path=output_path,
    )