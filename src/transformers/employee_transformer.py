from datetime import datetime
from typing import Any


def transform_employees_data(
    employees: list[dict[str, str]]
) -> list[dict[str, Any]]:
    """
    Transform employee records into a standardized format.
    """

    transformed_employees: list[dict[str, Any]] = []

    for employee in employees:

        transformed_employee = {
            "employee_id": int(
                employee["employee_id"]
            ),
            "first_name": employee["first_name"].strip().title(),
            "last_name": employee["last_name"].strip().title(),
            "email": employee["email"].strip().lower(),
            "department": employee["department"].strip(),
            "designation": employee["designation"].strip(),
            "joining_date": datetime.strptime(
                employee["joining_date"].strip(),
                "%Y-%m-%d",
            ).date(),
            "employment_type": employee["employment_type"].strip().title(),
            "status": employee["status"].strip().title(),
        }

        transformed_employees.append(
            transformed_employee
        )

    return transformed_employees


if __name__ == "__main__":
    pass