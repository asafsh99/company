import person as p


class Employee(p.Person):
    def __init__(self, e_id: int, firstname: str, lastname: str, address, phone_number: int, gender: str, salary: int,
                 seniority: int):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender)
        self.__salary = salary
        self.__seniority = seniority

    def __str__(self):
        return f'{super().__str__()},{self.__salary},{self.__seniority}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (super().__eq__(other)
                and isinstance(other, Employee)
                and self.__salary == other.__salary
                and self.__seniority == other.__seniority)

    def __hash__(self):
        return hash((super().__hash__(), self.__salary, self.__seniority))

    def to_csv(self):
        return super().to_csv() + [self.__salary, self.__seniority]
