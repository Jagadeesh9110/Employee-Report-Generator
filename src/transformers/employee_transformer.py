from pathlib import Path
from datetime import datetime
from typing import Any

def transform_employees_data(employees: list[dict[str, str]]) -> list[dict[str, Any]]:
    """
    Transform employee records into a standardized format.

    This function performs non-destructive transformations on
    validated employee records. It standardizes text fields by
    removing unnecessary whitespace and normalizing casing where
    appropriate.

    Args:
        employees: List of validated employee records.

    Returns:
        A list of transformed employee records.
    """

    transformed_employees: list[dict[str, Any]] = []

    for employee in employees:
        transformed_employee = {
            "employee_id": int(employee["employee_id"]),
            "first_name": employee["first_name"].strip().title(),
            "last_name": employee["last_name"].strip().title(),
            "gender": employee["gender"].strip().title(),
            "date_of_birth": datetime.strptime(
                employee["date_of_birth"].strip(),
                "%Y-%m-%d",
            ).date(),
            "email": employee["email"].strip().lower(),
            "phone_number": employee["phone_number"].strip(),
            "department": employee["department"].strip(),
            "designation": employee["designation"].strip(),
            "employment_type": employee["employment_type"].strip().title(),
            "employment_status": employee["employment_status"].strip().title(),
            "joining_date": datetime.strptime(
                employee["joining_date"].strip(),
                "%Y-%m-%d",
            ).date(),
            "manager_id": (
                int(employee["manager_id"])
                if employee["manager_id"].strip()
                else None
            ),
            "city": employee["city"].strip().title(),
            "state": employee["state"].strip().title(),
        }

        transformed_employees.append(transformed_employee)

    return transformed_employees


if __name__ == "__main__":
    pass