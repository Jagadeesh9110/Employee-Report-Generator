
"""
Generate salary dataset using employees.csv and attendance.csv.

Output:
    data/faker/salary.csv
"""

import csv
from pathlib import Path

CSV_HEADER = [
        "salary_id",
        "employee_id",
        "month",
        "basic_salary",
        "hra",
        "special_allowance",
        "overtime_pay",
        "gross_salary",
        "tax_deduction",
        "pf_deduction",
        "leave_deduction",
        "total_deductions",
        "net_salary",
]


DESIGNATION_SALARY = {
    "Software Engineer": 70000,
    "Senior Software Engineer": 95000,
    "Tech Lead": 120000,
    "Engineering Manager": 150000,
    "Accountant": 50000,
    "Financial Analyst": 65000,
    "Finance Manager": 90000,
    "HR Executive": 45000,
    "HR Manager": 80000,
    "Talent Acquisition Specialist": 60000,
    "Marketing Executive": 50000,
    "Marketing Specialist": 65000,
    "Digital Marketing Analyst": 70000,
    "Sales Executive": 50000,
    "Sales Manager": 90000,
    "Business Development Executive": 60000,
    "Operations Analyst": 55000,
    "Operations Executive": 65000,
    "Operations Manager": 95000,
    "Support Engineer": 50000,
    "Customer Success Executive": 55000,
    "Support Lead": 75000,
    "System Administrator": 70000,
    "Network Engineer": 80000,
    "DevOps Engineer": 110000,
}


def generate_data():


    BASE_DIR = Path(__file__).resolve().parents[2]

    EMPLOYEE_FILE = BASE_DIR / "data" / "faker" / "employees.csv"
    ATTENDANCE_FILE = BASE_DIR / "data" / "faker" / "attendance.csv"
    OUTPUT_FILE = BASE_DIR / "data" / "faker" / "salary.csv"

    # Store designation for each employee
    employees = {}

    with open(EMPLOYEE_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees[row["employee_id"]] = row["designation"]

    salary_records = []
    salary_id = 1

    with open(ATTENDANCE_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            employee_id = row["employee_id"]
            designation = employees[employee_id]

            basic_salary = DESIGNATION_SALARY[designation]

            # Fixed monthly allowances
            hra = round(basic_salary * 0.20, 2)
            special_allowance = round(basic_salary * 0.15, 2)

            # Attendance details
            working_days = int(row["working_days"])
            absent_days = int(row["absent_days"])
            overtime_hours = int(row["overtime_hours"])

            # Overtime payment
            overtime_pay = overtime_hours * 500

            gross_salary = (
                basic_salary
                + hra
                + special_allowance
                + overtime_pay
            )

            # Provident Fund
            pf_deduction = round(basic_salary * 0.12, 2)

            # Tax slab
            if gross_salary < 60000:
                tax_rate = 0.05
            elif gross_salary <= 100000:
                tax_rate = 0.10
            else:
                tax_rate = 0.15

            tax_deduction = round(gross_salary * tax_rate, 2)

            # Deduct salary only for absent days
            daily_salary = basic_salary / working_days
            leave_deduction = round(
                daily_salary * absent_days,
                2,
            )

            total_deductions = round(
                tax_deduction
                + pf_deduction
                + leave_deduction,
                2,
            )

            net_salary = round(
                gross_salary - total_deductions,
                2,
            )

            salary_records.append([
                salary_id,
                employee_id,
                row["month"],
                basic_salary,
                hra,
                special_allowance,
                overtime_pay,
                round(gross_salary, 2),
                tax_deduction,
                pf_deduction,
                leave_deduction,
                total_deductions,
                net_salary,
            ])

            salary_id += 1

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.writer(file)
        writer.writerow(CSV_HEADER)
        writer.writerows(salary_records)

    print(f"Generated {len(salary_records)} salary records.")
    print(f"Output File: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_data()
