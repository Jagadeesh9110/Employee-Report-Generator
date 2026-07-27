# Dataset Design Document

## Project

**Employee Report Generator**

A synthetic HR analytics dataset built using pure Python to simulate a company's employee, attendance, and salary records. The dataset is designed for practicing Data Engineering concepts such as data ingestion, ETL pipelines, SQL, reporting, and dashboard development.

---

# Project Architecture

```
employee-report-generator/
│
├── data/
│   └── python/
│       ├── employees.csv
│       ├── attendance.csv
│       └── salary.csv
│
├── scripts/
│   └── python/
│       ├── generate_employees.py
│       ├── generate_attendance.py
│       └── generate_salary.py
│
├── src/
│
├── docs/
│   └── dataset_design.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dataset Overview

The project contains three related datasets.

| Dataset | Description | Records |
|----------|-------------|---------|
| employees.csv | Master employee information | 100 |
| attendance.csv | Monthly attendance records | Variable (depends on joining date) |
| salary.csv | Monthly salary details | Same as attendance |

The three datasets together simulate a simplified HR Management System.

---

# Dataset Relationships

```
                employees.csv
                     │
        employee_id (Primary Key)
                     │
          ┌──────────┴──────────┐
          │                     │
          │                     │
attendance.csv            salary.csv
          │                     │
 employee_id FK          employee_id FK
```

Relationship Type

```
Employee
   │
   ├──────────────► Attendance
   │                 (One-to-Many)
   │
   └──────────────► Salary
                     (One-to-Many)
```

One employee can have multiple attendance records.

One employee can have multiple salary records.

Salary records are generated using attendance records.

---

# employees.csv

## Purpose

Stores the master details of every employee.

Each employee appears exactly once.

---

## Primary Key

```
employee_id
```

---

## Columns

| Column | Type | Description |
|---------|------|-------------|
| employee_id | Integer | Unique employee ID |
| first_name | String | Employee first name |
| last_name | String | Employee last name |
| gender | String | Male/Female |
| email | String | Company email |
| phone | String | Contact number |
| department | String | Department |
| designation | String | Job title |
| employment_type | String | Full-Time, Contract, Intern |
| joining_date | Date | Employee joining date |
| status | String | Active/Resigned/On Leave |
| city | String | Employee location |

---

# Business Rules

- Employee IDs start from 1001.
- Email addresses are unique.
- Joining dates are between 2020 and 2025.
- Designation depends on department.
- Employee appears only once.

---

# attendance.csv

## Purpose

Stores monthly attendance information for every employee.

Generated from employees.csv.

---

## Primary Key

```
attendance_id
```

---

## Foreign Key

```
employee_id
```

References

```
employees.employee_id
```

---

## Columns

| Column | Type | Description |
|---------|------|-------------|
| attendance_id | Integer | Unique attendance record |
| employee_id | Integer | Employee reference |
| month | YYYY-MM | Attendance month |
| working_days | Integer | Weekdays in month |
| present_days | Integer | Days present |
| leave_days | Integer | Approved leave |
| absent_days | Integer | Unapproved absence |
| late_days | Integer | Late arrivals |
| expected_working_hours | Integer | Working days × 8 |
| actual_working_hours | Integer | Actual worked hours |
| overtime_hours | Integer | Extra working hours |
| attendance_percentage | Float | Attendance percentage |

---

# Business Rules

Attendance is generated only for the year:

```
2025
```

Employees joining before 2025 receive attendance from January.

Employees joining during 2025 receive attendance beginning from their joining month.

Employees joining after 2025 are ignored.

Working days include only Monday-Friday.

Attendance quality is randomly categorized into:

- Excellent
- Good
- Average
- Poor

Attendance percentage

```
Present Days / Working Days × 100
```

---

# salary.csv

## Purpose

Stores monthly salary details generated from employee and attendance data.

Generated using

```
employees.csv
```

and

```
attendance.csv
```

---

## Primary Key

```
salary_id
```

---

## Foreign Key

```
employee_id
```

References

```
employees.employee_id
```

---

## Columns

| Column | Type | Description |
|---------|------|-------------|
| salary_id | Integer | Unique salary record |
| employee_id | Integer | Employee reference |
| month | YYYY-MM | Salary month |
| basic_salary | Decimal | Monthly base salary |
| hra | Decimal | House Rent Allowance |
| special_allowance | Decimal | Fixed allowance |
| overtime_pay | Decimal | Overtime payment |
| gross_salary | Decimal | Total earnings |
| tax_deduction | Decimal | Income tax |
| pf_deduction | Decimal | Provident Fund |
| leave_deduction | Decimal | Salary deducted for absences |
| total_deductions | Decimal | Total deductions |
| net_salary | Decimal | Final salary |

---

# Salary Calculation Rules

## Basic Salary

Depends on employee designation.

---

## HRA

```
20% of Basic Salary
```

---

## Special Allowance

```
15% of Basic Salary
```

---

## Overtime Pay

```
Overtime Hours × 500
```

---

## Gross Salary

```
Basic Salary
+ HRA
+ Special Allowance
+ Overtime Pay
```

---

## Provident Fund

```
12% of Basic Salary
```

---

## Tax Slabs

| Gross Salary | Tax |
|--------------|-----|
| Less than 60000 | 5% |
| 60000–100000 | 10% |
| Above 100000 | 15% |

---

## Leave Deduction

Calculated only for absent days.

```
Daily Salary × Absent Days
```

where

```
Daily Salary =
Basic Salary / Working Days
```

---

## Total Deductions

```
Tax
+ PF
+ Leave Deduction
```

---

## Net Salary

```
Gross Salary
− Total Deductions
```

---

# Synthetic Data Generation Rules

The datasets are generated using predefined business assumptions to simulate a realistic HR Management System.

## Employee Generation Rules

- Employee IDs start from **1001** and increment sequentially.
- Every employee has a unique email address.
- Phone numbers are randomly generated using valid Indian mobile prefixes.
- Joining dates are randomly assigned between **2020 and 2025**.
- Each employee belongs to exactly one department.
- Every department has a predefined set of valid designations.
- Employment type is randomly assigned as Full-Time, Contract, or Intern.
- Employee status is generated as Active, On Leave, or Resigned.
- Cities are selected from a predefined list of office locations.

---

## Attendance Generation Rules

Attendance records are generated only for the year **2025**.

Attendance generation follows these rules:

- Employees joining before 2025 receive attendance from January.
- Employees joining during 2025 receive attendance beginning from their joining month.
- Employees joining after 2025 are excluded.
- Working days include only Monday to Friday.
- Present, leave, and absent days always sum to the total working days.
- Attendance quality is randomly categorized as:
  - Excellent
  - Good
  - Average
  - Poor
- Expected working hours are calculated as:

```
Working Days × 8
```

- Actual working hours depend on attendance and overtime.
- Overtime hours are generated only for eligible attendance records.

---

## Salary Generation Rules

Salary records are generated directly from employee and attendance data.

Business rules include:

- Basic salary is determined by employee designation.
- HRA is fixed at 20% of the basic salary.
- Special Allowance is fixed at 15% of the basic salary.
- Overtime pay is calculated using overtime hours.
- PF deduction is fixed at 12% of the basic salary.
- Tax deduction follows predefined salary slabs.
- Leave deduction is calculated only for absent days.
- Gross salary, total deductions, and net salary are calculated automatically.
- One salary record is generated for every attendance record.

---

## Dataset Consistency Rules

The generators enforce the following consistency constraints:

- Employee IDs remain unique across all datasets.
- Attendance cannot exist without an employee.
- Salary cannot exist without attendance.
- Foreign keys always reference valid employee records.
- Duplicate primary keys are not generated.
- Every salary record corresponds to a valid attendance record.
- Dataset relationships remain consistent throughout generation.


# Data Flow

```
employees.csv
        │
        │
        ▼
generate_attendance.py
        │
        ▼
attendance.csv
        │
        │
        ▼
generate_salary.py
        │
        ▼
salary.csv
```

---

# Data Integrity

Primary keys are unique.

Foreign keys always reference valid employees.

Attendance is generated only for valid employees.

Salary is generated only from attendance records.

No salary record exists without an attendance record.

No attendance record exists without an employee.

---

# Possible Analytics

This dataset can be used to answer questions such as:

- Total employees by department
- Average salary by department
- Highest paid employees
- Attendance trends
- Overtime analysis
- Monthly payroll
- Employee distribution by city
- Salary expenditure by department
- Leave analysis
- Tax and PF summaries
- Payroll reporting
- HR dashboards

---

# Future Improvements

Possible future enhancements include:

- Promotions and salary hikes
- Bonus calculations
- Performance ratings
- Employee resignations during the year
- Holiday calendar integration
- Shift-based attendance
- Multiple office locations
- Increment history
- Payroll history across years
- Department transfers

---

# Learning Objectives

This dataset is suitable for practicing:

- Python
- CSV Processing
- Data Cleaning
- ETL Pipelines
- SQL
- Joins
- Aggregations
- Window Functions
- Data Validation
- Dashboard Development
- Power BI
- Tableau
- Data Warehousing
- Data Engineering Projects