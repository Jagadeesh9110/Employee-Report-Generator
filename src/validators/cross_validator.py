def validate_cross_records(
    employees: list[dict[str, str]],
    attendance_records: list[dict[str, str]],
    salary_records: list[dict[str, str]]
) -> list[str]:
    """
    Validate relationships between employee, attendance,
    and salary records.

    Args:
        employees: Employee records.
        attendance_records: Attendance records.
        salary_records: Salary records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    employee_ids = {
        employee["employee_id"].strip()
        for employee in employees
        if employee.get("employee_id", "").strip()
    }

    attendance_employee_ids = set()

    salary_employee_ids = set()

    # Attendance -> Employee
    for row_number, record in enumerate(attendance_records, start=2):
        employee_id = record.get("employee_id", "").strip()

        if employee_id:
            attendance_employee_ids.add(employee_id)

            if employee_id not in employee_ids:
                errors.append(
                    f"Attendance Row {row_number}: Employee ID '{employee_id}' does not exist."
                )

    # Salary -> Employee
    for row_number, record in enumerate(salary_records, start=2):
        employee_id = record.get("employee_id", "").strip()

        if employee_id:
            salary_employee_ids.add(employee_id)

            if employee_id not in employee_ids:
                errors.append(
                    f"Salary Row {row_number}: Employee ID '{employee_id}' does not exist."
                )

    # Employee -> Attendance
    for employee_id in employee_ids:
        if employee_id not in attendance_employee_ids:
            errors.append(
                f"Employee '{employee_id}' has no attendance record."
            )

    # Employee -> Salary
    for employee_id in employee_ids:
        if employee_id not in salary_employee_ids:
            errors.append(
                f"Employee '{employee_id}' has no salary record."
            )

    return errors


if __name__ == "__main__":
    pass