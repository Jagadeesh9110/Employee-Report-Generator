
import re


def validate_salary(salary_records: list[dict[str, str]]) -> list[str]:
    """
    Validate salary records.

    Args:
        salary_records: List of salary records.

    Returns:
        A list of validation error messages.
    """

    errors = []

    salary_ids = {}
    salary_keys = {}

    for row_number, record in enumerate(salary_records, start=2):

        # Validate Salary ID
        salary_id = record.get("salary_id", "").strip()

        if not salary_id:
            errors.append(f"Row {row_number}: Salary ID is missing.")
        else:
            try:
                int(salary_id)

                if salary_id in salary_ids:
                    errors.append(
                        f"Row {row_number}: Duplicate Salary ID '{salary_id}'."
                    )
                else:
                    salary_ids[salary_id] = row_number

            except ValueError:
                errors.append(
                    f"Row {row_number}: Salary ID must be a valid integer."
                )

        # Validate Employee ID
        employee_id = record.get("employee_id", "").strip()

        if not employee_id:
            errors.append(
                f"Row {row_number}: Employee ID is missing."
            )
        else:
            try:
                int(employee_id)
            except ValueError:
                errors.append(
                    f"Row {row_number}: Employee ID must be a valid integer."
                )

        # Validate Month
        month = record.get("month", "").strip()

        if not month:
            errors.append(
                f"Row {row_number}: Month is missing."
            )
        elif not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", month):
            errors.append(
                f"Row {row_number}: Month '{month}' must be in YYYY-MM format."
            )

        # Check Duplicate Salary Record
        if employee_id and month:
            key = (employee_id, month)

            if key in salary_keys:
                errors.append(
                    f"Row {row_number}: Duplicate salary record for Employee ID '{employee_id}' and Month '{month}'."
                )
            else:
                salary_keys[key] = row_number

        # Validate Salary Fields
        values = {}

        salary_fields = [
            ("basic_salary", True),
            ("hra", False),
            ("special_allowance", False),
            ("overtime_pay", False),
            ("gross_salary", True),
            ("tax_deduction", False),
            ("pf_deduction", False),
            ("leave_deduction", False),
            ("total_deductions", False),
            ("net_salary", True),
        ]

        for field, must_be_positive in salary_fields:

            value = record.get(field, "").strip()

            if not value:
                errors.append(
                    f"Row {row_number}: {field.replace('_', ' ').title()} is missing."
                )
                values[field] = None
                continue

            try:
                value = float(value)

                if must_be_positive:
                    if value <= 0:
                        errors.append(
                            f"Row {row_number}: {field.replace('_', ' ').title()} must be greater than 0."
                        )
                elif value < 0:
                    errors.append(
                        f"Row {row_number}: {field.replace('_', ' ').title()} cannot be negative."
                    )

                values[field] = value

            except ValueError:
                errors.append(
                    f"Row {row_number}: {field.replace('_', ' ').title()} must be a valid number."
                )
                values[field] = None

        # Validate Gross Salary
        if all(values[name] is not None for name in [
            "basic_salary",
            "hra",
            "special_allowance",
            "overtime_pay",
            "gross_salary",
        ]):
            expected_gross_salary = round(
                values["basic_salary"]
                + values["hra"]
                + values["special_allowance"]
                + values["overtime_pay"],
                2,
            )

            if abs(values["gross_salary"] - expected_gross_salary) > 0.01:
                errors.append(
                    f"Row {row_number}: Gross Salary should be {expected_gross_salary:.2f}."
                )

        # Validate Total Deductions
        if all(values[name] is not None for name in [
            "tax_deduction",
            "pf_deduction",
            "leave_deduction",
            "total_deductions",
        ]):
            expected_total_deductions = round(
                values["tax_deduction"]
                + values["pf_deduction"]
                + values["leave_deduction"],
                2,
            )

            if abs(values["total_deductions"] - expected_total_deductions) > 0.01:
                errors.append(
                    f"Row {row_number}: Total Deductions should be {expected_total_deductions:.2f}."
                )

        # Validate Net Salary
        if (
            values["gross_salary"] is not None
            and values["total_deductions"] is not None
            and values["net_salary"] is not None
        ):
            expected_net_salary = round(
                values["gross_salary"]
                - values["total_deductions"],
                2,
            )

            if abs(values["net_salary"] - expected_net_salary) > 0.01:
                errors.append(
                    f"Row {row_number}: Net Salary should be {expected_net_salary:.2f}."
                )

    return errors


if __name__ == "__main__":
    pass
