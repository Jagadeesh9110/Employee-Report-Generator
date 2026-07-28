def validate_salary(salary_records: list[dict[str, str]]) -> list[str]:
    """
    Validate salary records.

    Args:
        salary_records: List of salary records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    employee_ids = {}

    for row_number, record in enumerate(salary_records, start=2):
        # Validate Employee ID
        employee_id = record.get("employee_id", "").strip()
        if not employee_id:
            errors.append(f"Row {row_number}: Employee ID is missing.")
        else:
            if employee_id in employee_ids:
                errors.append(
                    f"Row {row_number}: Duplicate Employee ID '{employee_id}'."
                )
            else:
                employee_ids[employee_id] = row_number

        # Validate Basic Salary
        basic_salary = record.get("basic_salary", "").strip()
        if not basic_salary:
            errors.append(f"Row {row_number}: Basic Salary is missing.")
        else:
            try:
                basic_salary = float(basic_salary)

                if basic_salary <= 0:
                    errors.append(
                        f"Row {row_number}: Basic Salary must be greater than 0."
                    )
            except ValueError:
                errors.append(
                    f"Row {row_number}: Basic Salary must be a valid number."
                )

        # Validate Bonus
        bonus = record.get("bonus", "").strip()
        if not bonus:
            errors.append(f"Row {row_number}: Bonus is missing.")
        else:
            try:
                bonus = float(bonus)

                if bonus < 0:
                    errors.append(
                        f"Row {row_number}: Bonus cannot be negative."
                    )
            except ValueError:
                errors.append(
                    f"Row {row_number}: Bonus must be a valid number."
                )

        # Validate Deductions
        deductions = record.get("deductions", "").strip()
        if not deductions:
            errors.append(f"Row {row_number}: Deductions are missing.")
        else:
            try:
                deductions = float(deductions)

                if deductions < 0:
                    errors.append(
                        f"Row {row_number}: Deductions cannot be negative."
                    )
            except ValueError:
                errors.append(
                    f"Row {row_number}: Deductions must be a valid number."
                )

        # Validate Net Salary
        net_salary = record.get("net_salary", "").strip()
        if not net_salary:
            errors.append(f"Row {row_number}: Net Salary is missing.")
        else:
            try:
                net_salary = float(net_salary)

                if (
                    isinstance(basic_salary, float)
                    and isinstance(bonus, float)
                    and isinstance(deductions, float)
                ):
                    expected_salary = (
                        basic_salary + bonus - deductions
                    )

                    if net_salary != expected_salary:
                        errors.append(
                            f"Row {row_number}: Net Salary should be {expected_salary:.2f}, but found {net_salary:.2f}."
                        )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Net Salary must be a valid number."
                )

    return errors


if __name__ == "__main__":
    pass