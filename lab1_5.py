def check_multiple(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password(input_string: str):
    if input_string == "Python123":
        return "access granted"
    else:
        return "access denied"

def calculate_federal_tax(salary: int):
    if salary > 95375:
        return (salary / 100) * 24
    elif salary > 44725:
        return (salary / 100) * 22
    elif salary > 11000:
        return (salary / 100) * 12
    else:
        return (salary / 100) * 10
    