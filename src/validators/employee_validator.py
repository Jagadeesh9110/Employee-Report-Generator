import re


def validate_employees(
    employees: list[dict[str, str]]
) -> list[str]:
    """
    Validate employee records.

    Args:
        employees: List of employee records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    employee_ids = {}
    email_addresses = {}

    email_pattern = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    for row_number, employee in enumerate(
        employees,
        start=2,
    ):

        # Employee ID
        employee_id = employee.get(
            "employee_id",
            "",
        ).strip()

        if not employee_id:
            errors.append(
                f"Row {row_number}: Employee ID is missing."
            )

        elif employee_id in employee_ids:
            errors.append(
                f"Row {row_number}: Duplicate Employee ID '{employee_id}'."
            )

        else:
            employee_ids[employee_id] = row_number

        # First Name
        if not employee.get(
            "first_name",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: First Name is missing."
            )

        # Last Name
        if not employee.get(
            "last_name",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Last Name is missing."
            )

        # Email
        email = employee.get(
            "email",
            "",
        ).strip()

        if not email:
            errors.append(
                f"Row {row_number}: Email is missing."
            )

        else:

            if not email_pattern.fullmatch(email):
                errors.append(
                    f"Row {row_number}: Invalid email '{email}'."
                )

            email_key = email.lower()

            if email_key in email_addresses:
                errors.append(
                    f"Row {row_number}: Duplicate email '{email}'."
                )

            else:
                email_addresses[email_key] = row_number

        # Department
        if not employee.get(
            "department",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Department is missing."
            )

        # Designation
        if not employee.get(
            "designation",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Designation is missing."
            )

        # Joining Date
        if not employee.get(
            "joining_date",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Joining Date is missing."
            )

        # Employment Type
        if not employee.get(
            "employment_type",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Employment Type is missing."
            )

        # Status
        if not employee.get(
            "status",
            "",
        ).strip():
            errors.append(
                f"Row {row_number}: Status is missing."
            )

    return errors


if __name__ == "__main__":
    pass