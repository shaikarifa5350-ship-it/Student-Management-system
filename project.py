class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self, name, age, roll_no, course, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
        self.marks = marks
    def display_student(self):
        print("\n----- Student Details -----")
        self.display_person()
        print("Roll No:", self.roll_no)
        print("Course:",self.course)
        print("Marks:", self.marks)
    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:;
            print("Result: Fail")

# Taking input from user
name = input("Enter Name: ")
age = int(input("Enter Age: "))
roll_no = int(input("Enter Roll No: "))
course = input("Enter Course: ")
marks = int(input("Enter Marks: "))

# Creating Student object
student = Student(name, age, roll_no, course, marks)

# Displaying details
student.display_student()
student.result()