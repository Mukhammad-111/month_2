class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'FULL_NAME: {self.full_name} AGE: {self.age} IS_MARRIED: {self.is_married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = dict(marks)

    def average_mark(self):
        average = sum(self.marks.values()) / len(self.marks.keys())
        print(f'AVERAGE MARK: {average}')


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
            if self.experience > 3:
                while self.experience > 3:
                    bonus = (5 / 100) * Teacher.base_salary
                    Teacher.base_salary += bonus
                    self.experience -= 1
                print(f'YOU HAVE A SALARY WITH A BONUS: {Teacher.base_salary:.1f}')
            else:
                print(f'DO YOU HAVE A REGULAR SALARY: {Teacher.base_salary}')


teacher = Teacher('id', 23, False, 10)
teacher.introduce_myself()
teacher.salary()


def create_students(*args):
    students_list = []
    for student in args:
        students_list.append(student)
    return students_list

my_students = create_students(Student('nari', 23, False, {'bio': 5, 'math': 4, 'geo': 4}),
                Student('Mask', 22, True, {'bio': 4, 'math': 3, 'geo': 4}),
                Student('ali', 23, False, {'bio': 5, 'math': 5, 'geo': 3}))

for student in my_students:
    student.introduce_myself()
    print(student.marks)
    student.average_mark()