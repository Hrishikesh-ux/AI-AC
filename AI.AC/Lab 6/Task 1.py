class student:
    def __init__(self, name, rollno, marks):
        self.studentName = name
        self.studentRollNo = rollno
        self.studentMarks = marks

    def display_details(self):
        """Method to display student details"""
        print(f"Name: {self.studentName}, Roll No: {self.studentRollNo}, Marks: {self.studentMarks}, Grade: {self.calculate_grade()}")

    def calculate_grade(self):
        """Method to calculate grade based on marks"""
        if self.studentMarks >= 90:
            return 'A'
        elif self.studentMarks >= 80:
            return 'B'
        elif self.studentMarks >= 70:
            return 'C'
        elif self.studentMarks >= 60:
            return 'D'
        else:
            return 'F'


# Create student objects and display their details
student1 = student("fakhruddin", 1, 85)
student1.display_details()
student2 = student("zaidyen", 2, 92)
student2.display_details()
        