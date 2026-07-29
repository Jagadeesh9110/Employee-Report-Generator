# Employee Report Generator

## Overview

Employee Report Generator is a Python-based Data Engineering project that simulates an HR Management System by generating realistic employee, attendance, and salary datasets.

In addition to synthetic dataset generation, the project implements a complete ETL (Extract, Transform, Load) pipeline that validates raw datasets, transforms them into standardized Python objects, merges related records, and generates management-ready reports.

The project provides two independent implementations for synthetic data generation:

- Python Standard Library
- Faker Library

Both implementations produce identical dataset schemas while following the same business rules and relationships. The generated datasets can be used for ETL pipelines, SQL querying, reporting, dashboard development, and data validation.

The project emphasizes clean architecture, modular programming, structured data generation, logging, exception handling, and maintainable code.

---

# Problem Statement

Employee information in many organizations is distributed across multiple systems. Employee details, attendance records, payroll information, and department data are often maintained separately.

Preparing management reports requires combining data from multiple sources, validating records, performing calculations, and generating summaries. As organizations grow, this manual process becomes increasingly time-consuming and error-prone.

Common challenges include:

- Employee data stored across multiple files.
- Manual payroll calculations.
- Attendance and salary inconsistencies.
- Repetitive report preparation.
- Lack of standardized datasets for analytics.
- Difficulty validating relationships between datasets.

An automated solution is required to generate consistent, realistic datasets that can serve as the foundation for analytics and reporting.

---

# Proposed Solution

The Employee Report Generator automates the creation of synthetic HR datasets using Python.

The application:

- Generates employee master data.
- Creates realistic monthly attendance records.
- Calculates employee salaries using business rules.
- Maintains relationships across datasets.
- Produces clean CSV files suitable for ETL and analytics.
- Provides a foundation for future report generation and dashboard development.

The ETL pipeline also performs:

- Dataset validation using business rules.
- Data transformation into strongly typed Python objects.
- Cross-dataset validation.
- Dataset merging.
- Report generation.
- CSV export of management reports.

---

# Project Architecture

```text
employee-report-generator/
│
├── data/
│   ├── faker/
│   └── python/
│
├── docs/
│   └── dataset_design.md
│
├── output/
│   ├── employee_report.csv
│   ├── attendance_report.csv
│   ├── salary_report.csv
│   └── summary_report.csv
│
├── scripts/
│   ├── faker/
│   └── python/
│
├── src/
│   ├── pipeline/
│   │   └── validation_pipeline.py
│   │
│   ├── readers/
│   │   ├── employee_reader.py
│   │   ├── attendance_reader.py
│   │   └── salary_reader.py
│   │
│   ├── validators/
│   │   ├── employee_validator.py
│   │   ├── attendance_validator.py
│   │   ├── salary_validator.py
│   │   └── cross_validator.py
│   │
│   ├── transformers/
│   │   ├── employee_transformer.py
│   │   ├── attendance_transformer.py
│   │   ├── salary_transformer.py
│   │   └── merge_transformer.py
│   │
│   ├── reports/
│   │   ├── employee_report.py
│   │   ├── attendance_report.py
│   │   ├── salary_report.py
│   │   └── summary_report.py
│   │
│   └── main.py
│
├── utils/
│   └── csv_writer.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

# Dataset Generation Approaches

The project supports two independent implementations for generating the same HR datasets.

| Implementation | Description |
|---------------|-------------|
| Python Standard Library | Generates synthetic datasets using only Python's built-in libraries. |
| Faker Library | Generates realistic employee information using the Faker library while preserving the same schema and business rules. |

Both implementations generate identical dataset structures. The only difference is the method used to generate employee information.

---

# Current Features

The project currently supports:

### Dataset Generation

- Generate employee master dataset.
- Generate monthly attendance records.
- Generate monthly salary records.
- Generate realistic synthetic HR data.
- Maintain relationships between datasets.
- Calculate attendance metrics.
- Calculate payroll components.
- Support both Python Standard Library and Faker-based dataset generation.
- Document dataset schema and business logic.
- Generate CSV datasets automatically.

### Validation

- Apply business validation rules.
- Validate employee, attendance, and salary datasets.
- Perform cross-dataset validation.

### Transformation

- Read datasets through dedicated reader modules.
- Transform CSV data into Python data types.
- Merge employee, attendance, and salary records.

### Reporting

- Generate employee reports.
- Generate attendance reports.
- Generate salary reports.
- Generate summary reports.
- Export reports as CSV files.

---

# Datasets

The project generates three related CSV datasets:

| Dataset | Description |
|---------|-------------|
| employees.csv | Master employee information |
| attendance.csv | Monthly attendance records |
| salary.csv | Monthly salary records |

Detailed dataset schemas, relationships, and business rules are documented in **docs/dataset_design.md**.

---

# Dataset Relationships

```text
employees.csv
      │
      │ employee_id
      │
      ├────────────► attendance.csv
      │
      └────────────► salary.csv
```

Relationship Type

- One Employee → Many Attendance Records
- One Employee → Many Salary Records

Salary records are generated using attendance records.

---

# Business Workflow

```text
Generate Employees
          │
          ▼
employees.csv
          │
          ▼
Generate Attendance
          │
          ▼
attendance.csv
          │
          ▼
Generate Salary
          │
          ▼
salary.csv
```

---

# ETL Pipeline

```text
Employee Dataset
Attendance Dataset
Salary Dataset
        │
        ▼
CSV Readers
        │
        ▼
Validators
        │
        ▼
Transformers
        │
        ▼
Merge Transformer
        │
        ▼
Business Records
        │
        ▼
Report Generation
        │
        ▼
Output Reports
```

After generating the datasets, the application processes them through the following stages:

1. Read raw CSV datasets.
2. Validate records using business rules.
3. Transform raw string values into appropriate Python data types.
4. Merge employee, attendance, and salary information.
5. Generate management reports.
6. Export reports as CSV files.

---

# Output Reports

The ETL pipeline generates the following reports inside the `output/` directory.

| Report | Description |
|---------|-------------|
| employee_report.csv | Employee master report |
| attendance_report.csv | Attendance report |
| salary_report.csv | Salary report |
| summary_report.csv | Overall project summary |

---

# Technologies Used

## Programming Language

- Python 3

## Standard Libraries

- csv
- pathlib
- datetime
- calendar
- random
- json
- logging
- collections

## Development Tools

- Git
- GitHub
- Visual Studio Code

## Third-Party Libraries

- Faker

---

# Business Logic Highlights

## Employee Dataset

- Unique employee IDs.
- Department-based designations.
- Unique email addresses.
- Random joining dates.
- Multiple employment types.
- Employee status tracking.

---

## Attendance Dataset

- Attendance generated only for 2025.
- Employees joining during 2025 receive attendance from their joining month.
- Working days calculated using weekdays.
- Attendance quality categories:
  - Excellent
  - Good
  - Average
  - Poor
- Overtime generation.
- Attendance percentage calculation.

---

## Salary Dataset

- Salary based on designation.
- HRA = 20% of Basic Salary.
- Special Allowance = 15% of Basic Salary.
- Overtime Pay = Overtime Hours × 500.
- PF = 12% of Basic Salary.
- Tax calculated using salary slabs.
- Leave deduction based on absent days.
- Net salary automatically calculated.

---

# Project Status

## Current Progress

- ✅ Requirement Analysis
- ✅ Project Structure Design
- ✅ Employee Dataset Generation
- ✅ Attendance Dataset Generation
- ✅ Salary Dataset Generation
- ✅ Dataset Documentation
- ✅ Data Validation Pipeline
- ✅ Data Transformation Pipeline
- ✅ Dataset Merge Pipeline
- ✅ Report Generation
- ✅ CSV Export
- 🚧 Analytics Module
- 🚧 Testing

---

# Learning Objectives

This project demonstrates practical knowledge of:

- Python Programming
- Object-Oriented Programming
- File Handling
- CSV Processing
- JSON Processing
- Modular Project Design
- Exception Handling
- Logging
- Data Validation
- Business Logic Implementation
- Synthetic Data Generation
- Git & GitHub Workflow

---

# Future Roadmap

Upcoming features include:

- Department-wise Analytics
- Interactive Dashboard
- PostgreSQL Integration
- Pandas-based Data Processing
- Configuration using JSON
- Unit Testing
- Docker Support
- Apache Airflow Integration
- Exception Reporting
- Logging Improvements
- Dashboard-ready outputs

---

# How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd employee-report-generator
```

Generate datasets:
### Python Standard Library Implementation

```bash
python scripts/python/generate_employees.py
python scripts/python/generate_attendance.py
python scripts/python/generate_salary.py
```

Generated datasets:

```text
data/python/
```

### Faker Implementation

```bash
python scripts/faker/generate_employees.py
python scripts/faker/generate_attendance.py
python scripts/faker/generate_salary.py
```

Generated datasets:

```text
data/faker/
```

### Run the Complete ETL Pipeline

```bash
python src/main.py
```

Generated reports will be available in:

```text
output/
```

---

# Project Goals

This project is part of a structured learning roadmap to master Data Engineering fundamentals using only core Python before introducing external libraries.

The generated datasets will serve as the foundation for future work involving:

- ETL Pipelines
- SQL
- PostgreSQL
- Pandas
- Data Cleaning
- Dashboard Development
- Data Warehousing
- Analytics
- Data Engineering Projects