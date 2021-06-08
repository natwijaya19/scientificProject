class Employee:

    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+ last+'@company.com'

        Employee.num_emps +=1

    def fullname(self):
        return f'{self.first} {self.last}' #'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

#%%

emp1 = Employee('Kiki','Mulyadi', 50000)
emp2 = Employee('Test','User', 60000)

#%%
print(emp1.email)
print(emp2.email)

#%%
print(emp1.fullname())
print(Employee.fullname(emp1))


#%%
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


#%%
Employee.raise_amount = 1.06
emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

#%%
print(emp1.__dict__)
print(Employee.num_emps)
