import re


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
    attendance_ids = {}

    for row_number, record in enumerate(attendance_records, start=2):

        # Validate Attendance ID
        attendance_id = record.get("attendance_id", "").strip()

        if not attendance_id:
            errors.append(
                f"Row {row_number}: Attendance ID is missing."
            )
        elif attendance_id in attendance_ids:
            errors.append(
                f"Row {row_number}: Duplicate Attendance ID '{attendance_id}'."
            )
        else:
            attendance_ids[attendance_id] = row_number

        # Validate Employee ID
        employee_id = record.get("employee_id", "").strip()

        if not employee_id:
            errors.append(
                f"Row {row_number}: Employee ID is missing."
            )

        # Validate Month
        month = record.get("month", "").strip()

        if not month:
            errors.append(
                f"Row {row_number}: Month is missing."
            )
        elif not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", month):
            errors.append(
                f"Row {row_number}: Month '{month}' must be in YYYY-MM format."
            )

        # Check Duplicate Attendance Record
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
            errors.append(
                f"Row {row_number}: Working Days is missing."
            )
            working_days = None
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
                working_days = None

        # Validate Present Days
        present_days = record.get("present_days", "").strip()

        if not present_days:
            errors.append(
                f"Row {row_number}: Present Days is missing."
            )
            present_days = None
        else:
            try:
                present_days = int(present_days)

                if present_days < 0:
                    errors.append(
                        f"Row {row_number}: Present Days cannot be negative."
                    )

                if (
                    working_days is not None
                    and present_days > working_days
                ):
                    errors.append(
                        f"Row {row_number}: Present Days cannot exceed Working Days."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Present Days must be a valid integer."
                )
                present_days = None

        # Validate Leave Days
        leave_days = record.get("leave_days", "").strip()

        if not leave_days:
            errors.append(
                f"Row {row_number}: Leave Days is missing."
            )
            leave_days = None
        else:
            try:
                leave_days = int(leave_days)

                if leave_days < 0:
                    errors.append(
                        f"Row {row_number}: Leave Days cannot be negative."
                    )

                if (
                    working_days is not None
                    and leave_days > working_days
                ):
                    errors.append(
                        f"Row {row_number}: Leave Days cannot exceed Working Days."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Leave Days must be a valid integer."
                )
                leave_days = None

        # Validate Absent Days
        absent_days = record.get("absent_days", "").strip()

        if not absent_days:
            errors.append(
                f"Row {row_number}: Absent Days is missing."
            )
            absent_days = None
        else:
            try:
                absent_days = int(absent_days)

                if absent_days < 0:
                    errors.append(
                        f"Row {row_number}: Absent Days cannot be negative."
                    )

                if (
                    working_days is not None
                    and absent_days > working_days
                ):
                    errors.append(
                        f"Row {row_number}: Absent Days cannot exceed Working Days."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Absent Days must be a valid integer."
                )
                absent_days = None

        # Validate Late Days
        late_days = record.get("late_days", "").strip()

        if not late_days:
            errors.append(
                f"Row {row_number}: Late Days is missing."
            )
        else:
            try:
                late_days = int(late_days)

                if late_days < 0:
                    errors.append(
                        f"Row {row_number}: Late Days cannot be negative."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Late Days must be a valid integer."
                )

        # Validate Expected Working Hours
        expected_working_hours = record.get(
            "expected_working_hours",
            "",
        ).strip()

        if not expected_working_hours:
            errors.append(
                f"Row {row_number}: Expected Working Hours is missing."
            )
        else:
            try:
                expected_working_hours = int(expected_working_hours)

                if (
                    working_days is not None
                    and expected_working_hours != working_days * 8
                ):
                    errors.append(
                        f"Row {row_number}: Expected Working Hours should be {working_days * 8}."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Expected Working Hours must be a valid integer."
                )

        # Validate Actual Working Hours
        actual_working_hours = record.get(
            "actual_working_hours",
            "",
        ).strip()

        if not actual_working_hours:
            errors.append(
                f"Row {row_number}: Actual Working Hours is missing."
            )
        else:
            try:
                actual_working_hours = int(actual_working_hours)

                if actual_working_hours < 0:
                    errors.append(
                        f"Row {row_number}: Actual Working Hours cannot be negative."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Actual Working Hours must be a valid integer."
                )

        # Validate Overtime Hours
        overtime_hours = record.get(
            "overtime_hours",
            "",
        ).strip()

        if not overtime_hours:
            errors.append(
                f"Row {row_number}: Overtime Hours is missing."
            )
        else:
            try:
                overtime_hours = int(overtime_hours)

                if overtime_hours < 0:
                    errors.append(
                        f"Row {row_number}: Overtime Hours cannot be negative."
                    )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Overtime Hours must be a valid integer."
                )

        # Validate Attendance Percentage
        attendance_percentage = record.get(
            "attendance_percentage",
            "",
        ).strip()

        if not attendance_percentage:
            errors.append(
                f"Row {row_number}: Attendance Percentage is missing."
            )
        else:
            try:
                attendance_percentage = float(attendance_percentage)

                if not (0 <= attendance_percentage <= 100):
                    errors.append(
                        f"Row {row_number}: Attendance Percentage must be between 0 and 100."
                    )

                if (
                    working_days is not None
                    and present_days is not None
                ):
                    expected_percentage = round(
                        (present_days / working_days) * 100,
                        2,
                    )

                    if attendance_percentage != expected_percentage:
                        errors.append(
                            f"Row {row_number}: Attendance Percentage should be {expected_percentage}."
                        )

            except ValueError:
                errors.append(
                    f"Row {row_number}: Attendance Percentage must be a valid number."
                )

        # Validate Attendance Totals
        if (
            working_days is not None
            and present_days is not None
            and leave_days is not None
            and absent_days is not None
        ):
            if (
                present_days
                + leave_days
                + absent_days
                != working_days
            ):
                errors.append(
                    f"Row {row_number}: Present Days + Leave Days + Absent Days must equal Working Days."
                )

    return errors


if __name__ == "__main__":
    pass