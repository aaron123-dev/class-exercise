import argparse
import csv
import sys
from pathlib import Path


#step1
import logging


def check_data(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    header = rows[0]
    data = rows[1:]
    missing_rows = []

    for row_number, row in enumerate(data, start=2):
        if any(value == "" for value in row):
            missing_rows.append(row_number)
    return header, data, missing_rows

#step2: setting up a logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
) 

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Check the quality of a CSV file."
)

parser.add_argument(
    "--input", "-i",
    required=True,
    help="CSV file to check"
)

parser.add_argument(
    "--output", "-o",
    default="data_quality.txt",
    help="Path to input CSV file"
)

parser.add_argument(
    "--verbose", "-v",
    action="store_true", 
    help="Show detailed DEBUG messages"
)


args = parser.parse_args()

#step3
logger.debug(f"Arguments parsed: filename={args.input}")

#Step 4
if not args.verbose:
    logger.setLevel(logging.INFO)


#step 5
p = Path(args.input)
if not p.is_file():
    print(f"File not found: '{args.input}'")
    sys.exit(1)
else:
    print(f"File validated: '{args.input}'")

#Step6

logger.debug(f"Loading data from:{args.input}")

header, data, missing_rows = check_data(args.input)
#Step7
logger.info(f"Loaded {len(data)} rows")


#Step 8
if len(data) == 0:
    logger.error("Input file contains no data; cannot continue")
    sys.exit(1)

#Step 8
for row_number in missing_rows:
    logger.warning(f"Row{row_number} has missing values")

with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")

logger.info(f"Report saved to {args.output}")