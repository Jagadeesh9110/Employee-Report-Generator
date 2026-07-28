"""
Generate a synthetic employee dataset using the Faker library.

Output:
    data/faker/employees.csv
"""

import random
import csv
from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta

# Use the Indian locale to generate realistic employee information.
fake = Faker("en_IN")


DEPARTMENTS = [
    "Engineering",
    "Finance",
    "Human Resources",
    "Marketing",
    "Sales",
    "Operations",
    "Customer Support",
    "IT",
]

DEPARTMENT_WEIGHTS = [
    35,  # Engineering
    10,  # Finance
    8,   # Human Resources
    10,  # Marketing
    15,  # Sales
    10,  # Operations
    7,   # Customer Support
    5,   # IT
]

DEPARTMENT_DESIGNATIONS = {
        "Engineering": [
            "Software Engineer",
            "Senior Software Engineer",
            "Tech Lead",
            "Engineering Manager",
        ],

        "Finance": [
            "Accountant",
            "Financial Analyst",
            "Finance Manager",
        ],

        "Human Resources": [
            "HR Executive",
            "HR Manager",
            "Talent Acquisition Specialist",
        ],

        "Marketing": [
            "Marketing Executive",
            "Marketing Specialist",
            "Digital Marketing Analyst",
        ],

        "Sales": [
            "Sales Executive",
            "Sales Manager",
            "Business Development Executive",
        ],

        "Operations": [
            "Operations Analyst",
            "Operations Executive",
            "Operations Manager",
        ],

        "Customer Support": [
            "Support Engineer",
            "Customer Success Executive",
            "Support Lead",
        ],

        "IT": [
            "System Administrator",
            "Network Engineer",
            "DevOps Engineer",
        ],
    }

EMPLOYMENT_TYPES = [
        "Full-Time",
        "Contract",
        "Intern",
]

EMPLOYMENT_TYPE_WEIGHTS = [
        70,
        20,
        10,
]

STATUS = [
        "Active",
        "Inactive",
]

STATUS_WEIGHTS = [
    90,
    10,
]

COMPANY_DOMAIN = "techcorp.com"

def generate_data():
    NUMBER_OF_EMPLOYEES = 100
    CSV_HEADER = [
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "department",
        "designation",
        "joining_date",
        "employment_type",
        "status",
    ]

    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_DIR = BASE_DIR / "data" / "faker"
    OUTPUT_FILE = DATA_DIR / "employees.csv"

    # Create the output directory if it doesn't exist. 
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    employees = []

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_difference = (end_date - start_date).days

    for employee_number in range(NUMBER_OF_EMPLOYEES):
        employee_id = 1001 + employee_number

        gender = random.choice(["Male", "Female"])
        
        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()
        
        last_name = fake.last_name()

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}@{COMPANY_DOMAIN}"
        )

        department = random.choices(DEPARTMENTS,
            weights=DEPARTMENT_WEIGHTS,
            k=1,
       )[0]

        designation = random.choice(
            DEPARTMENT_DESIGNATIONS[department]
        )

        joining_date = (
            start_date +
            timedelta(days=random.randint(0, date_difference))
        ).strftime("%Y-%m-%d")

        employment_type = random.choices(EMPLOYMENT_TYPES,
                weights=EMPLOYMENT_TYPE_WEIGHTS,
                k=1,
        )[0]

        status = random.choices(STATUS,
                weights=STATUS_WEIGHTS,
                k=1,
        )[0]

        employees.append([
            employee_id,
            first_name,
            last_name,
            email,
            department,
            designation,
            joining_date,
            employment_type,
            status,
        ])

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(CSV_HEADER)

        writer.writerows(employees)

        print(f"Successfully generated {NUMBER_OF_EMPLOYEES} employees.")
        print(f"Output File: {OUTPUT_FILE}")





if __name__==  "__main__":
    generate_data()