class Address:
    def __init__(self, street, number, city):
        self.__street = street
        self.__number = str(number)
        self.__city = city

    def __str__(self):
        return f'{self.__street},{self.__number},{self.__city}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (isinstance(other, Address)
                and self.__street == other.__street
                and self.__number == other.__number
                and self.__city == other.__city)

    def __hash__(self):
        return hash((self.__street, self.__number, self.__city))

    def to_csv(self):
        return [self.__street,self.__number,self.__city]