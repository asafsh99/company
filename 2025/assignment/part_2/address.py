from data_utils import validate_address_street, validate_address_city, validate_address_number


class Address:
    def __init__(self, street: str, number, city: str):
        self.__street = validate_address_street(street)
        self.__number = validate_address_number(number)
        self.__city = validate_address_city(city)

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
        return [self.__street, self.__number, self.__city]
