class Person:
    def __init__(self, e_id:int, firstname:str, lastname:str, address, phone_number=None, gender=None):
        self._e_id = e_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = f'{self._firstname}.{self._lastname}@email.com'
        self._address = address
        self._phone_number = phone_number
        self._gender = gender

    @property
    def id(self):
        return self._e_id

    def __eq__(self, other):
        return (isinstance(other, Person)
                and self._e_id == other.id
                and self._firstname == other._firstname
                and self._lastname == other._lastname
                and self._address == other._address
                and self._phone_number == other._phone_number
                and self._gender == other._gender)

    def __hash__(self):
        return hash((self._e_id, self._firstname,
                     self._lastname, self._email,
                     self._address, self._phone_number,
                     self._gender))

    def __str__(self):
        return (f'{self.__class__.__name__}: {self._e_id},{self._firstname},{self._lastname},{self._email},{self._address}'
                f',{self._phone_number},{self._gender}')

    def __repr__(self):
        return self.__str__()

    def to_csv(self):
        return [self.__class__.__name__,self._e_id, self._firstname, self._lastname] + self._address.to_csv() + [
            self._phone_number, self._gender]