import employee as e


class Salesperson(e.Employee):
    sales_counter = 0

    def __init__(self,e_id, firstname, lastname, address, phone_number, gender, salary, seniority,
                 sales_target:int,current_sales=0):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender, salary, seniority)
        self.__sales_target = sales_target
        self.__current_sales = current_sales if current_sales > 0 else 0
        Salesperson.sales_counter += self.__current_sales

    def __add__(self, amount):
        self.__current_sales += amount
        Salesperson.sales_counter += amount
        return self

    def __mod__(self, div):
        return (self.__current_sales / self.__sales_target)*div


    def __str__(self):
        return f'{super().__str__()},{self.__sales_target},{self.__current_sales}'

    def to_csv(self):
        return super().to_csv() + [self.__sales_target, self.__current_sales]
