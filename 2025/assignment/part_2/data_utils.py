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

    if gender == 'F' or gender == 'M':
        return gender



