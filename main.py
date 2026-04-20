class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        avg = sum(self.grades) / len(self.grades)
        print(f"O‘rtacha baho: {avg}")

    def info(self):
        print(f"Ism: {self.name}, Baholar: {self.grades}")


s1 = Student("Vali", [4, 5, 3, 5])
s1.average()
s1.info()
