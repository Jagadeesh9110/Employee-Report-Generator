import logging
from pathlib import Path

from src.readers.employee_reader import load_employees
from src.readers.attendance_reader import load_attendance
from src.readers.salary_reader import load_salary

from src.validators.employee_validator import validate_employees
from src.validators.attendance_validator import validate_attendance
from src.validators.salary_validator import validate_salary
from src.validators.cross_validator import validate_cross_records

from src.transformers.employee_transformer import (
    transform_employees_data,
)
from src.transformers.attendance_transformer import (
    transform_attendance_data,
)
from src.transformers.salary_transformer import (
    transform_salary_data,
)
from src.transformers.merge_transformer import (
    merge_employee_data,
)

from src.reports.employee_report import (
    generate_employee_report,
)
from src.reports.attendance_report import (
    generate_attendance_report,
)
from src.reports.salary_report import (
    generate_salary_report,
)
from src.reports.summary_report import (
    generate_summary_report,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def main() -> None:
    """Run the complete Employee Report Generator pipeline."""

    logging.info("Starting Employee Report Generator...")

    # Input Files
    employee_file = Path("data") / "python" / "employees.csv"
    attendance_file = Path("data") / "python" / "attendance.csv"
    salary_file = Path("data") / "python" / "salary.csv"

    # Output Files
    output_directory = Path("output")

    employee_report = output_directory / "employee_report.csv"
    attendance_report = output_directory / "attendance_report.csv"
    salary_report = output_directory / "salary_report.csv"
    summary_report = output_directory / "summary_report.csv"

    # Read Data
    logging.info("Loading datasets...")

    employees = load_employees(employee_file)
    attendance_records = load_attendance(attendance_file)
    salary_records = load_salary(salary_file)

    logging.info("Datasets loaded successfully.")

    # Validation
    logging.info("Running validation...")

    errors = []

    errors.extend(validate_employees(employees))
    errors.extend(validate_attendance(attendance_records))
    errors.extend(validate_salary(salary_records))
    errors.extend(
        validate_cross_records(
            employees,
            attendance_records,
            salary_records,
        )
    )

    if errors:
        logging.error("Validation failed.\n")

        for error in errors:
            logging.error(error)

        return

    logging.info("Validation completed successfully.")

    # Transformation
    logging.info("Transforming datasets...")

    transformed_employees = transform_employees_data(
        employees
    )

    transformed_attendance = transform_attendance_data(
        attendance_records
    )

    transformed_salary = transform_salary_data(
        salary_records
    )

    logging.info("Transformation completed successfully.")

    # Merge
    logging.info("Merging datasets...")

    merged_records = merge_employee_data(
        transformed_employees,
        transformed_attendance,
        transformed_salary,
    )

    logging.info("Merge completed successfully.")

    # Generate Reports

    logging.info("Generating reports...")

    generate_employee_report(
        merged_records,
        employee_report,
    )

    generate_attendance_report(
        merged_records,
        attendance_report,
    )

    generate_salary_report(
        merged_records,
        salary_report,
    )

    generate_summary_report(
        merged_records,
        summary_report,
    )

    logging.info("Reports generated successfully.")

    logging.info("Output directory: %s", output_directory.resolve())


if __name__ == "__main__":
    main()