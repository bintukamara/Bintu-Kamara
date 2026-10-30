
class Person:
    def __init__(self, name, student_id, age):
        if type(name) != str or not name.strip():
            raise ValueError("Name must be non-empty text.")
        if type(student_id) != str or not student_id.strip():
            raise ValueError("Student ID must be non-empty text.")
        if type(age) != int or age < 0:
            raise ValueError("Age must be a non-negative whole number.")
        self.name = name.strip()
        self.student_id = student_id.strip()
        self.age = age

    def update_name(self, new_name):
        if type(new_name) != str or not new_name.strip():
            raise ValueError("Name must be non-empty text.")
        self.name = new_name.strip()

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Age:", self.age)


class Student(Person):
    total_students = 0

    def __init__(self, name, student_id, age, course, score):
        if type(course) != str or not course.strip():
            raise ValueError("Course must be non-empty text.")
        if not self.is_valid_score(score):
            raise ValueError("Score must be a number from 0 to 100.")
        super().__init__(name, student_id, age)
        self.course = course.strip()
        self.score = score
        Student.total_students += 1

    def update_score(self, new_score):
        if not self.is_valid_score(new_score):
            raise ValueError("Score must be a number from 0 to 100.")
        self.score = new_score

    def get_result(self):
        # Demonstration rule, not an official university grading policy.
        if self.score >= 50:
            return "Pass"
        return "Needs improvement"

    def compare_score(self, other_student):
        # Two Student objects interact through this method.
        if not isinstance(other_student, Student):
            raise ValueError("Compare with another Student object.")
        if self.score > other_student.score:
            return self.name + " has the higher score."
        if self.score < other_student.score:
            return other_student.name + " has the higher score."
        return "Both students have the same score."

    def display_info(self):
        super().display_info()
        print("Course:", self.course)
        print("Score:", self.score)
        print("Result:", self.get_result())

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_valid_score(score):
        return (type(score) == int or type(score) == float) and 0 <= score <= 100


# One list stores all records added to the system.
students = []


def add_student(student):
    if not isinstance(student, Student):
        print("Only Student objects can be added.")
        return
    for existing_student in students:
        if existing_student.student_id == student.student_id:
            print("That student ID already exists.")
            return
    students.append(student)
    print("Student added:", student.student_id)


def display_students():
    if not students:
        print("No student records.")
        return
    for student in students:
        print("\n--- Student result ---")
        student.display_info()


# Create and store two fictional Student objects.
student1 = Student("Alieu Kamara", "S001", 21, "Python OOP", 45)
student2 = Student("Hawa Conteh", "S002", 20, "Networking", 82)

add_student(student1)
add_student(student2)

# Demonstrate instance methods that change one object's information.
student1.update_name("Alieu A. Kamara")
student1.update_score(68)

display_students()

# Demonstrate interaction between two objects.
# These scores are compared only to demonstrate object interaction.
print("\nObject interaction:", student1.compare_score(student2))

# Demonstrate the class method and static method.
print("Total Student objects created:", Student.get_total_students())
print("Is 105 a valid score?", Student.is_valid_score(105))
