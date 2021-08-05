import datetime
from figures import circles as c

class Person:

    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def __str__(self):
        return f'This is {self.name} str'


    def __repr__(self):
        return f'Person(name={self.name}, yob={self.yob})'

    def get_age(self):
        return datetime.date.today().year - self.yob



class Student(Person):

    def __init__(self, name, yob, university, major):
        # Person.__init__(self, name, yob)
        super().__init__(name, yob)
        self.university = university
        self.major = major


    def introduce(self):
        return f'My name is {self.name} and I study {self.major}'


if __name__ == '__main__':
    # juan = Person("Juan", 1987, "male")
    # print(juan)
    # print(f'My age is {juan.get_age()}')
    # juan_student = Student("Juan", 1987, "UP", "Engineering")
    # print(juan_student.introduce())
    # print(juan_student.get_age())
    # print(juan_student)
    my_circle = c.Dimension(3)
    print(my_circle.diameter())