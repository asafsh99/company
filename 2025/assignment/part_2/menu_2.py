class Menu:
    def __init__(self, options=None, title='---- MENU ----'):
        if options is None:
            options = []
        self.__options = options
        self.__title = title

    def __str__(self):
        st = f'\n{self.__title}\n'
        for i, option in enumerate(self.__options):
            st += f"{i + 1}.\t{option[0]}\n"
        return st

    def is_valid_input(self, choice):
        return choice.isdigit() and int(choice) in range(1, len(self.__options) + 1)

    def show(self):
        if self.__options:
            print(self.__str__())
            choice = input(f'Enter your choice (1 - {len(self.__options)}): ')
            if self.is_valid_input(choice):
                option = self.__options[int(choice) - 1]
                option[1](option[2])
            else:
                print(f'Invalid input! Please choose number option from the menu: (1 - {len(self.__options)})')
        else:
            print('Sorry, but no options provided...')
            exit()
