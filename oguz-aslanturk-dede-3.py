# Mehmet OGUZ
# Hatice Berna ASLANTURK
# Cagdas DEDE

# HOMEWORK QUESTION 3


def run():
    excuse_file = open('personnel_excuse_list.txt', 'r')
    line = excuse_file.readline()
    excuse_list = []

    while line != '':
        line = excuse_file.readline()
        if line != '':
            personnel_excuses = line.split(',')
        excuse_list.append(personnel_excuses)

    excuse_file.close()

    day = get_working_day()
    if day == 0:
        return

    working_hour_begins = get_shift_start()
    working_hour_ends = get_shift_end(working_hour_begins)

    available_personnel = find_available_personnel(excuse_list, day, working_hour_begins, working_hour_ends)
    print_result(available_personnel)


def get_working_day():
    print_days()
    while True:
        try:
            shift_day = int(input("Please type shift day: "))
        except ValueError:
            print("Please enter a valid day 0-7")
        if 0 <= shift_day <= 7:
            return shift_day
        else:
            print('Shift day should be in the range 1-7')


def get_shift_start():
    while True:
        try:
            shift_start = int(input("Please type shift beginning hour: "))
        except ValueError:
            print("Please enter a valid day 0-7")
        if 0 <= shift_start <= 23:
            return shift_start
        else:
            print('Shift start should be in the range 0-23')


def get_shift_end(working_hour_begins):
    while True:
        try:
            shift_end = int(input("Please type shift end hour: "))
        except ValueError:
            print("Please enter a valid day 0-7")
        if working_hour_begins < shift_end <= 23:
            return shift_end
        else:
            print(f'Shift end should be in the range {working_hour_begins}-23')


def print_result(available_personnel):
    print("Available personnel for this shift: ")

    for personnel in available_personnel:
        print(personnel)


def print_days():
    print("Monday : 1")
    print("Tuesday : 2")
    print("Wednesday : 3")
    print("Thursday : 4")
    print("Friday : 5")
    print("Saturday : 6")
    print("Sunday : 7")
    print("Exit : 0")


def find_available_personnel(excuse_list, day, working_hour_begins, working_hour_ends):
    available_personnels = []

    for personnel_excuse_list in excuse_list:
        if check_personnel_status(personnel_excuse_list[day], working_hour_begins, working_hour_ends ):
            available_personnels.append(personnel_excuse_list[0])

    return available_personnels


def check_personnel_status(personnel_excuse_hours, working_hour_begins, working_hour_ends):
    hours = personnel_excuse_hours.split('-')
    excuse_hour_begins = int(hours[0])
    excuse_hour_ends = int(hours[1])

    if excuse_hour_ends <= working_hour_begins:
        return True
    if working_hour_ends <= excuse_hour_begins:
        return True

    return False


run()