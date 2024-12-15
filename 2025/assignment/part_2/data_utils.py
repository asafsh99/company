# check phone number
def validate_phone_number(number):
    if number is None:
        return None

    if len(number) == 11 and number[:2] == "05" and number[2].isdigit() and number[3] == "-" and number[4:].isdigit():
        return number
    else:
        return None


# check gender
def validate_gender(gender):
    if gender is None:
        return None

    if gender == 'F' or gender == 'M':
        return gender
    else:
        return None

# check years_experience

