import employee as e


class Salesperson(e.Employee):
    sales_counter = 0

    def __init__(self,e_id, firstname, lastname, address, phone_number, gender, salary, seniority,
                 sales_target,current_sales=0):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender, salary, seniority)
        self.__sales_target = sales_target
        self.__current_sales = current_sales if current_sales > 0 else 0
        # self.__sales = Salesperson.sales_counter
        Salesperson.sales_counter += self.__current_sales

    def __add__(self, other):
        self.__current_sales += other
        Salesperson.sales_counter +=other
        return self




    def __str__(self):
        return f'{super().__str__()},{self.__sales_target},{self.__current_sales}'

    def to_csv(self):
        return super().to_csv() + [self.__sales_target, self.__current_sales]
