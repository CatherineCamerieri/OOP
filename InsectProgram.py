import InsectClass as c

def main():
    mosquito = c.Insect('mosquito',2,4)
    housefly = c.Insect('housefly',2,4)

    mosquito.calculate_flight()
    housefly.calculate_flight()

    print(f'The {mosquito.get_name()} can fly up to {mosquito.get_flight_miles()} miles')

    print(f'The {housefly.get_name()} can fly up to {housefly.get_flight_miles()} miles')

main()