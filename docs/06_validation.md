# Validation Layer Documentation

## Overview

The Validation Layer is responsible for verifying the quality, correctness, and consistency of the data after it has been loaded by the Reader Layer.

The Reader Layer is responsible only for reading CSV files and converting them into Python objects (`list[dict]`).

The Validation Layer ensures that the loaded data satisfies the required business rules before any transformation or report generation begins.

---

# Validation Flow

```
CSV Files
    │
    ▼
Reader Layer
    │
    ▼
Python Objects (list[dict])
    │
    ▼
Validation Layer
    │
    ▼
Validation Errors
```

Each validator receives data from the Reader Layer, performs validations, and returns a list of validation errors.

The validators never stop at the first error. Instead, they collect all errors and return them together.

---

# Validation Strategy

Instead of raising exceptions for invalid data, validators return a list of error messages.

Example:

```python
errors = validate_employees(employee_records)

if errors:
    for error in errors:
        print(error)
```

This approach allows users to identify every problem in a single execution instead of fixing one error at a time.

---

# Employee Validator

File:

```
src/validators/employee_validator.py
```

Purpose:

Validates individual employee records.

## Validation Rules

### Required Fields

- Employee ID cannot be empty.
- First Name cannot be empty.
- Last Name cannot be empty.
- Department cannot be empty.
- Email cannot be empty.

### Duplicate Validation

- Duplicate Employee IDs are not allowed.
- Duplicate Email Addresses are not allowed.

### Email Validation

- Email address must follow a valid email format.

Example:

```
john.doe@company.com
```

Invalid examples:

```
john@
john.com
@company.com
```

---

# Attendance Validator

File:

```
src/validators/attendance_validator.py
```

Purpose:

Validates attendance records.

## Validation Rules

### Required Fields

- Employee ID
- Month
- Working Days
- Present Days

### Numeric Validation

Working Days

- Must be an integer.
- Must be greater than zero.

Present Days

- Must be an integer.
- Cannot be negative.
- Cannot exceed Working Days.

### Duplicate Validation

Each employee can have only one attendance record per month.

Duplicate combinations of

```
(Employee ID, Month)
```

are not allowed.

---

# Salary Validator

File:

```
src/validators/salary_validator.py
```

Purpose:

Validates salary records.

## Validation Rules

### Required Fields

- Employee ID
- Basic Salary
- Bonus
- Deductions
- Net Salary

### Numeric Validation

Basic Salary

- Must be numeric.
- Must be greater than zero.

Bonus

- Must be numeric.
- Cannot be negative.

Deductions

- Must be numeric.
- Cannot be negative.

Net Salary

- Must be numeric.

### Business Rule

Net Salary must satisfy

```
Net Salary = Basic Salary + Bonus − Deductions
```

### Duplicate Validation

Duplicate Employee IDs are not allowed in the salary dataset.

---

# Cross Validator

File:

```
src/validators/cross_validator.py
```

Purpose:

Validates relationships between multiple datasets.

Unlike the previous validators, this validator compares multiple datasets instead of validating a single file.

It ensures referential integrity between the Employee, Attendance, and Salary datasets.

## Validation Rules

### Attendance → Employee

Every attendance record must reference an existing employee.

Example:

```
Attendance

EMP001
EMP002
EMP999
```

If EMP999 does not exist in employees.csv, it is reported as an error.

---

### Salary → Employee

Every salary record must reference an existing employee.

Example:

```
Salary

EMP001
EMP005
```

If EMP005 does not exist in employees.csv, it is reported as an error.

---

### Employee → Attendance

Every employee should have an attendance record.

If an employee exists but has no attendance record, it is reported.

---

### Employee → Salary

Every employee should have a salary record.

If an employee exists but has no salary record, it is reported.

---

# Why Cross Validation?

Individual validators only validate a single dataset.

For example:

Employee Validator

```
employees.csv
```

Attendance Validator

```
attendance.csv
```

Salary Validator

```
salary.csv
```

None of these validators know about the contents of the other datasets.

The Cross Validator compares multiple datasets together to ensure they are consistent.

---

# Design Principles

The Validation Layer follows the Single Responsibility Principle (SRP).

Reader Layer

- Reads data.

Validation Layer

- Validates data.

Transformation Layer

- Modifies data.

Reporting Layer

- Generates reports.

Each layer has exactly one responsibility.

---

# Validation Output

Every validator returns

```python
list[str]
```

Example:

```python
[
    "Row 5: Employee ID is missing.",
    "Row 8: Invalid email format 'abc@'.",
    "Row 12: Duplicate Employee ID 'EMP1023'."
]
```

Returning all validation errors allows users to correct every issue in a single iteration.

---

# Validation Pipeline

```
employees.csv
attendance.csv
salary.csv
        │
        ▼
Readers
        │
        ▼
Employee Validator
Attendance Validator
Salary Validator
        │
        ▼
Cross Validator
        │
        ▼
Combined Validation Errors
```

The validation pipeline ensures that:

- Individual records are valid.
- Numeric values are correct.
- Duplicate records are detected.
- Business rules are satisfied.
- Relationships across datasets remain consistent.

Only after successful validation should the data proceed to the Transformation Layer.