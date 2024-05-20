#creat class
class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")


# A example to use:
student1 = Student("student1", "BMI", 80, 85, 90)
student1.print_details()  
# Output: Name:student1, Major:BMI, Code Portfolio Score:80, Group Project Score:85, Exam Score:90
