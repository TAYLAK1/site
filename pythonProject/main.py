class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        pass

class Manager:
    def __init__(self,name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_info(self):
        return f'Manager: {self.name}, Salary: {self.salary}, Department: {self.department}'

manager1 = Manager('Aidanek', 45000, 'Marketing')
print(manager1.department)
print(manager1.get_info())

class Intern(Manager):
    def __init__(self, name, salary, department, experience):
        super().__init__(name, salary, department)
        self.experience = experience
    def get_info(self):
        return f'Manager: {self.name}, Salary: {self.salary}, Department: {self.department}, Experience:{self.experience}'

inter1 = Intern('Timur', 30000, 'IT', 2)
print(inter1.name)
print(inter1.get_info())