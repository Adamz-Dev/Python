from abc import ABC, abstractmethod

class Payroll(ABC):
    @abstractmethod
    def get_payroll():
        pass



class Employee(ABC):

    id = 0
    first_name = ""
    last_name = ""
    role = ""
    is_active = True
    salary = 0
    email = ""
    phone_number = ""

class FullTimeEmployee(Employee, Payroll):
    def get_payroll(self):
        fixed_salary = 10000
        print(f"Employee name: {self.first_name} {self.last_name}")
        print(f"Net salary: {self.salary}")


class HourlyEmployee(Employee, Payroll):
    number_of_hours_worked = 5
    hourly_rate = 40
    def get_payroll(self):
        self.salary = self.number_of_hours_worked * self.hourly_rate
        print(f"Employee name: {self.first_name} {self.last_name}")
        print(f"Net salary: {self.salary}")

full_time = FullTimeEmployee()
full_time.salary = 10000
full_time.first_name = "Adamu"
full_time.last_name = "Nyawira"
full_time.get_payroll()

Part_time = HourlyEmployee()
Part_time.salary = 0
Part_time.first_name = "Habibu"
Part_time.last_name = "Musa"
Part_time.get_payroll()

