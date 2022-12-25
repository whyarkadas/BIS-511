# Mehmet OGUZ
# Hatice Berna ASLANTURK
# Cagdas DEDE

# HOMEWORK QUESTION 2

MIN_PARKING_HOUR = 2
UP_TO_TWO_HOUR_CHARGE = 3
PER_HOUR_CHARGE = 1
MAX_CHARGE = 20

def Run():
    charge_list = []
    parking_hour_list = []
    total_receipt = 0
    average_parking_hour = 0

    while True:
        parking_hour = GetParkingHour()

        if parking_hour == 0:
            print_result(total_receipt, average_parking_hour)
            return

        charge = DetermineCharges(parking_hour)
        print(f"Charge for {parking_hour} hour is : {charge}")

        parking_hour_list.append(parking_hour)
        charge_list.append(charge)

        total_receipt = TotalReceipt(charge_list)
        average_parking_hour = CalculateAverageParkingHour(parking_hour_list)

        print_result(total_receipt, average_parking_hour)


def DetermineCharges(hours_parked):
    if hours_parked <= MIN_PARKING_HOUR:
        charge = UP_TO_TWO_HOUR_CHARGE
    if hours_parked > MIN_PARKING_HOUR:
        charge = (hours_parked - MIN_PARKING_HOUR) * PER_HOUR_CHARGE + UP_TO_TWO_HOUR_CHARGE

    if charge > MAX_CHARGE:
        return MAX_CHARGE
    else:
        return charge


def GetParkingHour():
    while True:
        try:
            parking_hour = int(input("Please type parking hour (0 for exit): "))
        except ValueError:
            print("Please enter a valid integer 0-24")
            continue
        if 0 <= parking_hour <= 24:
            return parking_hour
        else:
            print('Parking hour should be in the range 1-24')


def TotalReceipt(charge_list):
    total_receipt = 0
    for charge in charge_list:
        total_receipt += charge

    return total_receipt


def CalculateAverageParkingHour(parking_hour_list):
    total_parkig_hour = 0
    for hour in parking_hour_list:
        total_parkig_hour += hour

    return total_parkig_hour / len(parking_hour_list)


def print_result(total_receipt, average_parking_hour):
    print("####### CUMULATIVE RESULT ######")
    print(f"Total receipt for yesterday is : {total_receipt}")
    print(f"Average parking hour is : {average_parking_hour:.2f}")
    print("################################")


Run()

