class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class EmployeeOne:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age

        self.obj_salary = Salary(pay, bonus)  # composition 

    def total_sal(self):
        return self.obj_salary.annual_salary()

emp = EmployeeOne('Geek', 25, 10000, 1500)

print(emp.total_sal())

                                Composition
-------------------------------------------------------------------------------------
                                Aggregation

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class EmployeeOne:

    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.agg_salary = sal  # Aggregation

    def total_sal(self):
        return self.agg_salary.annual_salary()

salary = Salary(10000, 1500)

emp = EmployeeOne('Geek', 25, salary)

print(emp.total_sal()) 
