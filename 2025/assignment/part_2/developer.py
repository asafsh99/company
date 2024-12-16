import employee as e


class Developer(e.Employee):
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender,
                 salary, seniority, programming_languages=None, experience_years=0):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender, salary, seniority)
        if isinstance(programming_languages, str):
            programming_languages = programming_languages.split(';')
        self.__programming_languages = programming_languages if programming_languages is not None else []
        self.__experience_years = experience_years if experience_years >= 0 else 0

    def __str__(self):
        return f'{super().__str__()},{self.__programming_languages},{self.__experience_years}'

    def __add__(self, language):
        if language not in self.__programming_languages:
            self.__programming_languages.append(language)
        return self.__programming_languages

    def __sub__(self, language):
        if language in self.__programming_languages and len(self.__programming_languages):
            self.__programming_languages.remove(language)
        return self.__programming_languages

    def __lt__(self, other):
        return len(self.__programming_languages) < len(other.__programming_languages)

    def to_csv(self):
        return super().to_csv() + [self.__programming_languages, self.__experience_years]
