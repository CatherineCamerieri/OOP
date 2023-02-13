import InsectClass as c

def main():
    insect_1 = c.Insect()

    insect_1.calculate_flight()

    print('The insect can fly', insect_1.get_flight_miles())

main()