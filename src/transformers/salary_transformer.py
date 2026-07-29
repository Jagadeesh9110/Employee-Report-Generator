from datetime import datetime
from typing import Any


def transform_salary_data(
    salary_records: list[dict[str, str]]
) -> list[dict[str, Any]]:
    """
    Transform salary records into a standardized format.

    This function converts string values into appropriate Python
    data types while standardizing the records for downstream
    processing.

    Args:
        salary_records: List of validated salary records.

    Returns:
        A list of transformed salary records.
    """

    transformed_salary: list[dict[str, Any]] = []

    for salary in salary_records:
        transformed_record = {
            "salary_id": int(salary["salary_id"]),
            "employee_id": int(salary["employee_id"]),
            "month": datetime.strptime(
                salary["month"].strip(),
                "%Y-%m",
            ).date(),
            "basic_salary": float(salary["basic_salary"]),
            "hra": float(salary["hra"]),
            "special_allowance": float(
                salary["special_allowance"]
            ),
            "overtime_pay": float(salary["overtime_pay"]),
            "gross_salary": float(salary["gross_salary"]),
            "tax_deduction": float(salary["tax_deduction"]),
            "pf_deduction": float(salary["pf_deduction"]),
            "leave_deduction": float(salary["leave_deduction"]),
            "total_deductions": float(
                salary["total_deductions"]
            ),
            "net_salary": float(salary["net_salary"]),
        }

        transformed_salary.append(transformed_record)

    return transformed_salary


if __name__ == "__main__":
    pass