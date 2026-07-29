import csv
from pathlib import Path
from typing import Any


def write_csv_report(
    rows: list[dict[str, Any]],
    fieldnames: list[str],
    output_path: Path,
) -> None:
    """
    Write a list of dictionaries to a CSV file.

    Args:
        rows: Data to be written.
        fieldnames: CSV column names.
        output_path: Destination file path.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        mode="w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)

