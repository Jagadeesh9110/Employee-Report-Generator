

def validate_employees(employees: list[dict[str, str]]) -> list[str]:
    """
    Validate employee records.

    Args:
        employees: List of employee records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    for row_number, employee in enumerate(employees, start=2):
        # Employee ID
        employee_id = employee.get("employee_id", "").strip()
        if not employee_id:
            errors.append(f"Row {row_number}: Employee ID is missing.")

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

    return errors


if __name__ == "__main__":
    pass