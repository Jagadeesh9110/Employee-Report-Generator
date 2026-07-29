# Transformation Layer

## Overview

The Transformation Layer is responsible for converting validated CSV data into standardized Python objects. After the Validation Layer ensures that the input data is correct, this layer performs type conversion and data standardization so that the rest of the application works with clean and consistent data.

Unlike the Validation Layer, no validation is performed here. The transformation layer assumes that all incoming records have already been validated.

---

## Folder Structure

```text
src/
│
├── transformers/
│   ├── employee_transformer.py
│   ├── attendance_transformer.py
│   ├── salary_transformer.py
│   └── merge_transformer.py
```

---

## Architecture

```text
                         Validation Layer
                                │
                                ▼
                 Validated Employee Records
                                │
                                ▼
                  employee_transformer.py
                                │
                                ▼
                Transformed Employee Records
                                │
                                │
                 Validated Attendance Records
                                │
                                ▼
                 attendance_transformer.py
                                │
                                ▼
              Transformed Attendance Records
                                │
                                │
                  Validated Salary Records
                                │
                                ▼
                   salary_transformer.py
                                │
                                ▼
                Transformed Salary Records
                                │
          ──────────────────────┼──────────────────────
                                │
                                ▼
                  merge_transformer.py
                                │
                                ▼
                   Merged Business Records
                                │
                                ▼
                    Report Generation Layer
```

---

## Responsibilities

The Transformation Layer is responsible for:

- Converting string values into appropriate Python data types.
- Standardizing text fields.
- Preserving the original meaning of the data.
- Producing clean business records for downstream processing.
- Merging transformed datasets into a unified business record.

---

## How It Works

### Step 1 – Receive Validated Records

Each transformer receives validated records from the Validation Layer.

```text
Validated Records
        │
        ▼
Transformer
```

---

### Step 2 – Transform Data

Each transformer converts raw CSV string values into appropriate Python data types while standardizing text fields.

Examples:

- `employee_id` → `int`
- `joining_date` → `date`
- `basic_salary` → `float`
- `attendance_percentage` → `float`
- `email` → lowercase
- `first_name` → title case

After transformation, every record contains proper Python objects instead of raw CSV strings.

---

### Step 3 – Return Transformed Records

Each transformer returns a new list containing transformed records.

```text
Raw CSV Strings
        │
        ▼
Transformation
        │
        ▼
Python Objects
```

---

### Step 4 – Merge Transformed Data

The Merge Transformer combines the transformed employee, attendance, and salary datasets using `employee_id` as the common key.

```text
Employee Records
        │
Attendance Records
        │
Salary Records
        │
        ▼
Merge Transformer
        │
        ▼
Merged Business Records
```

---

### Step 5 – Pass Data to the Next Layer

The merged business records become the input for the Report Generation Layer.

```text
Merged Business Records
          │
          ▼
Report Generation Layer
```

---

## Transformations Performed

### Employee Transformer

- Convert `employee_id` to `int`
- Convert `joining_date` to `date`
- Normalize employee names
- Convert email addresses to lowercase
- Remove unnecessary whitespace

### Attendance Transformer

- Convert numeric fields to `int` or `float`
- Convert `month` to `date`
- Standardize attendance-related values

### Salary Transformer

- Convert salary values to `float`
- Convert identifiers to `int`
- Convert `month` to `date`

### Merge Transformer

- Combine employee, attendance, and salary records
- Use `employee_id` as the common key
- Produce a unified business record for each employee

---

## Output

The Transformation Layer produces merged business records containing standardized Python objects. These records are then passed to the Report Generation Layer for business analytics and report creation.