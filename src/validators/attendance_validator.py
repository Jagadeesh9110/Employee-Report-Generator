def validate_attendance(attendance_records: list[dict[str, str]]) -> list[str]:
    """
    Validate attendance records.

    Args:
        attendance_records: List of attendance records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    attendance_keys = {}

    for row_number, record in enumerate(attendance_records, start=2):
        # Validate Employee ID
        employee_id = record.get("employee_id", "").strip()
        if not employee_id:
            errors.append(f"Row {row_number}: Employee ID is missing.")

        # Validate Month
        month = record.get("month", "").strip()
        if not month:
            errors.append(f"Row {row_number}: Month is missing.")

        # Check duplicate attendance record
        if employee_id and month:
            key = (employee_id, month)

            if key in attendance_keys:
                errors.append(
                    f"Row {row_number}: Duplicate attendance record for Employee ID '{employee_id}' and Month '{month}'."
                )
            else:
                attendance_keys[key] = row_number

        # Validate Working Days
        working_days = record.get("working_days", "").strip()
        if not working_days:
            errors.append(f"Row {row_number}: Working Days is missing.")
        else:
            try:
                working_days = int(working_days)

                if working_days <= 0:
                    errors.append(
                        f"Row {row_number}: Working Days must be greater than 0."
                    )
            except ValueError:
                errors.append(
                    f"Row {row_number}: Working Days must be a valid integer."
                )

        # Validate Present Days
        present_days = record.get("present_days", "").strip()
        if not present_days:
            errors.append(f"Row {row_number}: Present Days is missing.")
        else:
            try:
                present_days = int(present_days)

                if present_days < 0:
                    errors.append(
                        f"Row {row_number}: Present Days cannot be negative."
                    )

                if (
                    isinstance(working_days, int)
                    and present_days > working_days
                ):
                    errors.append(
                        f"Row {row_number}: Present Days cannot exceed Working Days."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Present Days must be a valid integer."
                )

    return errors


if __name__ == "__main__":
    pass