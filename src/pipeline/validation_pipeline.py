from pathlib import Path

from src.readers.employee_reader import load_employees
from src.readers.attendance_reader import load_attendance
from src.readers.salary_reader import load_salary


from src.validators.employee_validator import validate_employees
from src.validators.attendance_validator import validate_attendance
from src.validators.salary_validator import validate_salary
from src.validators.cross_validator import validate_cross_records

def run_validation_pipeline(
    employee_file: Path,
    attendance_file: Path,
    salary_file: Path,
) -> list[str]:
    """
    Run the complete validation pipeline.

    Args:
        employee_file: Path to employee CSV.
        attendance_file: Path to attendance CSV.
        salary_file: Path to salary CSV.

    Returns:
        A list of validation error messages.
    """
    # Read all datasets
    employees = load_employees(employee_file)
    attendance_records = load_attendance(attendance_file)
    salary_records = load_salary(salary_file)

    # Validate individual datasets
    employee_errors = validate_employees(employees)
    attendance_errors = validate_attendance(attendance_records)
    salary_errors = validate_salary(salary_records)

    # Validate relationships across datasets
    cross_errors = validate_cross_records(
        employees,
        attendance_records,
        salary_records,
    )

    # Combine all validation errors
    all_errors = (
        employee_errors
        + attendance_errors
        + salary_errors
        + cross_errors
    )

    return all_errors


if __name__ == "__main__":
    pass
