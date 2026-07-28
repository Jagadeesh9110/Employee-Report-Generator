

def validate_employees(employees: list[dict[str, str]]) -> list[str]:
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

    for row_number, employee in enumerate(employees, start=2):
        # Validate Employee ID
        employee_id = employee.get("employee_id", "").strip()
        if not employee_id:
            errors.append(f"Row {row_number}: Employee ID is missing.")
        else:
            if employee_id in employeesIds:
                errors.append(
                    f"Row {row_number}: Duplicate Employee ID '{employee_id}'."
                )
            else:
                employee_ids[employee_id] = row_number


        # First Name
        first_name = employee.get("first_name", "").strip()
        if not first_name:
            errors.append(f"Row {row_number}: First Name is missing.")

        # Last Name
        last_name = employee.get("last_name", "").strip()
        if not last_name:
            errors.append(f"Row {row_number}: Last Name is missing.")

        # Department
        department = employee.get("department", "").strip()
        if not department:
            errors.append(f"Row {row_number}: Department is missing.")

        # Email
        email = employee.get("email", "").strip()
        if not email:
            errors.append(f"Row {row_number}: Email is missing.")
        else:
            if not email_pattern.fullmatch(email):
                errors.append(
                    f"Row {row_number}: Invalid email format '{email}'."
                )

            email_key = email.lower()

            if email_key in email_addresses:
                errors.append(
                    f"Row {row_number}: Duplicate email address '{email}'."
                )
            else:
                email_addresses[email_key] = row_number

    return errors


if __name__ == "__main__":
    pass