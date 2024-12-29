class Manage:
    def __init__(self, company_name, address, employees=None):
        self.__company_name = company_name
        self._address = address
        self.employees = employees if employees is not None else []

    def __str__(self):
        return f'{self.__class__.__name__}:{self.__company_name},{self._address}'

    def __repr__(self):
        return self.__str__()

    def add_employee(self, new_employee):
        for employee in self.employees:
            if new_employee == employee:
                return False
        return True

    def remove_employee(self, check_id):
        for employee in self.employees:
            if employee.id == check_id:
                self.employees.remove(employee)
                return True
        return False

    def print_employees(self):
        print("Employees:")
        for emp in self.employees:
            print(emp)

    def __getitem__(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def to_csv(self):
        return [self.__company_name] + self._address.to_csv()
