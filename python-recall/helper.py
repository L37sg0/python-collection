from main import user_input


def days_to_units(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{days} days are {days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        unit = days_and_unit_dictionary['unit']
        condition_check = user_input_number > 0
        # we want to do conversions only for positive numbers
        if condition_check:
            my_var = days_to_units(user_input_number, unit)
            print(my_var)
        elif user_input_number == 0:
            print("you've entered 0 so no conversion for you!")
        else:
            print("you've entered negative number, so no conversion for you!")

    except ValueError:
        print("your input is not valid number, don't break my program!")

user_input_message = "Enter number of days and conversion unit column separated\n"