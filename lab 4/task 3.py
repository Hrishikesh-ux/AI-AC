student_data = {
    "personal": {
        "first_name": "Amit",
        "last_name": "Verma"
    },
    "academic": {
        "branch": "Computer Science",
        "results": {
            "SGPA": 8.7
        }
    }
}
# Expected Output: ("Amit Verma", "Computer Science", 8.7)
student_data = {
    "personal": {
        "first_name": "Neha",
        "last_name": "Singh"
    },
    "academic": {
        "branch": "Mechanical",
        "results": {
            "SGPA": 9.1
        }
    }
}
# Expected Output: ("Neha Singh", "Mechanical", 9.1)
def extract_student_info(student_data: dict) -> tuple:
    """
    Extracts full name, branch, and SGPA from nested student dictionary.

    Returns:
    - Tuple of (Full Name, Branch, SGPA)
    """
    first_name = student_data.get("personal", {}).get("first_name", "")
    last_name = student_data.get("personal", {}).get("last_name", "")
    full_name = f"{first_name} {last_name}".strip()

    branch = student_data.get("academic", {}).get("branch", "")
    sgpa = student_data.get("academic", {}).get("results", {}).get("SGPA", None)

    return (full_name, branch, sgpa)
extract_student_info(student_data)
# Output: ("Amit Verma", "Computer Science", 8.7)