from datetime import datetime
from typing import Any


def transform_attendance_data(
    attendance_records: list[dict[str, str]]
) -> list[dict[str, Any]]:
    """
    Transform attendance records into a standardized format.

    This function converts string values into appropriate Python
    data types while standardizing the records for downstream
    processing.

    Args:
        attendance_records: List of validated attendance records.

    Returns:
        A list of transformed attendance records.
    """

    transformed_attendance: list[dict[str, Any]] = []

    for attendance in attendance_records:
        transformed_record = {
            "attendance_id": int(attendance["attendance_id"]),
            "employee_id": int(attendance["employee_id"]),
            "month": datetime.strptime(
                attendance["month"].strip(),
                "%Y-%m",
            ).date(),
            "working_days": int(attendance["working_days"]),
            "present_days": int(attendance["present_days"]),
            "leave_days": int(attendance["leave_days"]),
            "absent_days": int(attendance["absent_days"]),
            "late_days": int(attendance["late_days"]),
            "expected_working_hours": int(
                attendance["expected_working_hours"]
            ),
            "actual_working_hours": int(
                attendance["actual_working_hours"]
            ),
            "overtime_hours": int(attendance["overtime_hours"]),
            "attendance_percentage": float(
                attendance["attendance_percentage"]
            ),
        }

        transformed_attendance.append(transformed_record)

    return transformed_attendance


if __name__ == "__main__":
    pass