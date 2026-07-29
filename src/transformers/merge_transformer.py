from typing import Any


def merge_employee_data(
    employees: list[dict[str, Any]],
    attendance_records: list[dict[str, Any]],
    salary_records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Merge employee, attendance, and salary records.

    Args:
        employees: Transformed employee records.
        attendance_records: Transformed attendance records.
        salary_records: Transformed salary records.

    Returns:
        List of merged employee records.
    """

    attendance_lookup = {
        attendance["employee_id"]: attendance
        for attendance in attendance_records
    }

    salary_lookup = {
        salary["employee_id"]: salary
        for salary in salary_records
    }

    merged_records: list[dict[str, Any]] = []

    for employee in employees:
        employee_id = employee["employee_id"]

        merged_record = {
            **employee,
            **attendance_lookup.get(employee_id, {}),
            **salary_lookup.get(employee_id, {}),
        }

        merged_records.append(merged_record)

    return merged_records


if __name__ == "__main__":
    pass