import csv

def analyze_csv(file_path: str) -> dict:
    """
    Reads a CSV file and returns:
    - Total number of rows
    - Number of empty rows
    - Total number of words across all cells
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            word_count += sum(len(cell.strip().split()) for cell in row)

    return {
        "total_rows": total_rows,
        "empty_rows": empty_rows,
        "word_count": word_count
    }

# Example:
# Input: 'students.csv'
# Output: {'total_rows': 100, 'empty_rows': 5, 'word_count': 1200}


# Example 1:
# Input: 'data.csv'
# Output: {'total_rows': 50, 'empty_rows': 3, 'word_count': 600}

# Example 2:
# Input: 'survey.csv'
# Output: {'total_rows': 200, 'empty_rows': 10, 'word_count': 2500}
