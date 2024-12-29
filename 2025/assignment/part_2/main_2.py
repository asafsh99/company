import csv
import address as ad
import manage as ma
import developer as dev
from menu_2 import Menu
import salesperson as sales


def get_company_data():
    company_file = open("company_2.csv", 'r')
    reader = csv.reader(company_file)
    next(reader)
    second_line = next(reader)
    addr = ad.Address(second_line[1], second_line[2], second_line[3])
    manage = ma.Manage(second_line[0], addr)
    next(reader)
    for row in reader:
        if row[0] == 'Developer':
            manage.employees.append(dev.Developer(row[1], row[2], row[3], ad.Address(row[4], row[5], row[6]), row[7],
                                                  row[8], row[9], row[10], row[11], int(row[12])))

        elif row[0] == 'Salesperson':
            manage.employees.append(
                sales.Salesperson(row[1], row[2], row[3], ad.Address(row[4], row[5], row[6]), row[7],
                                  row[8], row[9], row[10], int(row[11]), int(row[12])))
    return manage


def save_company_data(manage):
    with open("company_2_work.csv", "w", newline="") as company_file:
        writer = csv.writer(company_file)

        writer.writerow(["name", "street", "number", "city"])
        writer.writerow(manage.to_csv())

        writer.writerow(["department", "id", "firstname", "lastname", "address",
                         "phone_number", "gender", "salary", "seniority", "param1", "param2"])

        for employee in manage.employees:
            writer.writerow(employee.to_csv())


def print_company(manage):
    print(manage)


def print_employees(manage):
    manage.print_employees()


def add_new_employee(manage):
    employee_id = input("Enter the employee ID: ")
    firstname = input("Enter the first name: ")
    lastname = input("Enter the last name: ")
    street = input("Enter the street: ")
    number = input("Enter the street number: ")
    city = input("Enter the city: ")
    employee_address = ad.Address(street, number, city)
    phone_number = input("Enter the phone number (format: 05x-1234567):")
    gender = input("Enter the gender (M/F): ")
    salary = input("enter salary: ")
    seniority = input("enter seniority: ")
    department = input("Insert type of employee, d for Developer and s for Salesperson: ")
    if department == "d":
        programming_languages = input(f'insert programming languages separate by ;')
        experience_years = int(input('insert experience years: '))
        new_employee = dev.Developer(employee_id, firstname, lastname, employee_address, phone_number, gender,
                                     salary, seniority, programming_languages, experience_years)
    else:
        sales_target = input('enter sales target for this year: ')
        new_employee = sales.Salesperson(employee_id, firstname, lastname, employee_address, phone_number, gender,
                                         salary, seniority, sales_target)
    if manage.add_employee(new_employee):
        manage.employees.append(new_employee)
        print(f"Employee {firstname} {lastname} added successfully.")
    else:
        print("Employee could not be added. Check if the employee already exists.")


def remove_employee(manage):
    employee_id = input("insert employee id:")
    if manage.remove_employee(employee_id):
        print(f"Employee with ID {employee_id} removed successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")


def add_programming_language(manage):
    employee_id = input("Insert developer ID: ")
    developer = manage[employee_id]
    language = input("Insert programming language to add: ")
    if isinstance(developer, dev.Developer):
        update_dev = developer + language
        if update_dev:
            print(f"Updated developer language: {update_dev}")
        else:
            print('there is a problem with the language')
    else:
        print('the provided id not belong to developer')


def remove_programming_language(manage):
    employee_id = input("Insert developer ID: ")
    developer = manage[employee_id]
    language = input("Insert programming language to remove: ")
    update_dev = developer - language
    if update_dev:
        print(f"Updated developer language: {update_dev}")
    else:
        print('the id not found or left only one programming language')


def compare_developers(manage):
    employee_id_1 = input("Insert developer 1 ID: ")
    developer1 = manage[employee_id_1]
    employee_id_2 = input("Insert developer 2 ID: ")
    developer2 = manage[employee_id_2]

    if isinstance(developer1, dev.Developer) and isinstance(developer2, dev.Developer):
        result = developer1 > developer2
        print(result)
    else:
        print("One or both of the provided IDs do not belong to a Developer")


def compare_salesperson(manage):
    employee_id_1 = input("Insert developer 1 ID: ")
    salesperson1 = manage[employee_id_1]
    employee_id_2 = input("Insert developer 2 ID: ")
    salesperson2 = manage[employee_id_2]
    if isinstance(salesperson1, sales.Salesperson) and isinstance(salesperson2, sales.Salesperson):
        result = salesperson1 > salesperson2
        print(result)
    else:
        print("One or both of the provided IDs do not belong to a salesperson")


def add_sales(manage):
    employee_id = input("enter salesperson id: ")
    amount = int(input("enter amount of sales: "))
    salesperson = manage[employee_id]
    if isinstance(salesperson, sales.Salesperson):
        update_sel = salesperson + amount
        if update_sel:
            print(f"updated salesperson sales: {update_sel}")
        else:
            print('must enter valid amount')
    else:
        print('the provided id not belong to salesperson')


def get_sales_target(manage):
    employee_id = input("enter salesperson id: ")
    salesperson = manage[employee_id]
    if isinstance(salesperson, sales.Salesperson):
        salesperson % 100
    else:
        print('the provided id do not belong to a salesperson')


def exit_menu(manage):
    save_company_data(manage)
    print("Bye Bye!")
    exit()


def main():
    manage = get_company_data()
    menu_options = [
        ('Print company details', print_company, manage),
        ('Print all employees', print_employees, manage),
        ('Add new employee', add_new_employee, manage),
        ('Remove employee', remove_employee, manage),
        ('Add programming language to developer', add_programming_language, manage),
        ('Remove programming language from developer', remove_programming_language, manage),
        ('Compare 2 developers', compare_developers, manage),
        ('Add sales to salesperson', add_sales, manage),
        ('Get sales target of salesperson', get_sales_target, manage),
        ('Compare 2 salesperson', compare_salesperson, manage),
        ('EXIT', exit_menu, manage),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == '__main__':
    main()
