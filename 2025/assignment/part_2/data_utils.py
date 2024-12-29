# check phone number
def validate_phone_number(number):
    if number is None:
        return

    if len(number) == 11 and number[:2] == "05" and number[2].isdigit() and number[3] == "-" and number[4:].isdigit():
        return number


# check gender
def validate_gender(gender):
    if gender is None:
        return

    if gender in ['F', 'M']:
        return gender

# check id
def validate_id(e_id):
    if not e_id.isdigit() or len(e_id) != 9:
        return
    else:
        return e_id

# check first name
def validate_first_name(firs_name):
    if not firs_name.isalpha():
        return
    else:
        return firs_name

# check last name
def validate_last_name(last_name):
    if not last_name.isalpha():
        return
    else:
        return last_name

# check address
def validate_address_street(street):
    if not street.isalpha():
        return
    else:
        return street

# check address
def validate_address_city(city):
    if not city.replace("-","").isalpha() :
        return
    else:
        return city

#check address
def validate_address_number(number):
    if not number.replace("/","1").isdigit() :
        return
    else:
        return number


def validate_salary(salary):
    if not salary.isdigit():
        return
    else:
        return salary


def validate_seniority(seniority):
    if not seniority.isdigit():
        return
    else:
        return seniority