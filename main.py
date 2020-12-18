from distance_matrix import find_shortest_distance_truck, package_hash, return_to_hub
import truck


def start_route(car):
    """This function is in charge of creating the route each truck is going to take, first the truck will deliver
    any packages that need to be delivered by a specific time, then will deliver the rest of the packages"""
    # if truck has early packages deliver them first
    if len(car.get_early_packages()):
        while len(car.get_early_packages()) > 0:
            # find the shortest route to package
            distance, location = find_shortest_distance_truck(car.get_early_packages(), car.get_address())
            car.move(distance, location)
            car.deliver_package(car.get_early_packages())

        # deliver rest of packages
        if len(car.get_eod_packages()):
            while len(car.get_eod_packages()) > 0:
                distance, location = find_shortest_distance_truck(car.get_eod_packages(), car.get_address())
                car.move(distance, location)
                car.deliver_package(car.get_eod_packages())
        distance_to_hub, current_location = return_to_hub(car.get_address())
        car.move(distance_to_hub, current_location)
    else:
        while len(car.get_eod_packages()) > 0:
            distance, location = find_shortest_distance_truck(car.get_eod_packages(), car.get_address())
            car.move(distance, location)
            car.deliver_package(car.get_eod_packages())
    distance_to_hub, current_location = return_to_hub(car.get_address())
    car.move(distance_to_hub, current_location)


# get packages delivered by a user specified time if none have been delivered, show current status
def get_delivered_packages():
    print('Please enter when you want to see packages delivered.')
    try:
        hour = int(input('Please enter hour, in form of 24 hour clock. i.e 9am is 09, 10pm is 22: '))
    except ValueError as e:
        print('Please only enter the hour you wish to see')
        hour = int(input('Please enter hour, in form of 24 hour clock. i.e 9am is 09, 10pm is 22: '))
    minutes = int(input('Please enter minutes from 0 - 60:'))
    # list of all delivered packages if no say none have been delivered and print out status of all packages
    time_list = package_hash.print_delivered_by(hour, minutes)
    if len(time_list) > 0:
        for row in time_list:
            print(row)
    else:
        print('No packages have been delivered yet. Current status of packages: ')
        package_hash.print_status()


def correct_address(package_id, address, city, state, zipcode):
    """corrects an incorrect address for any package passed through to a new address"""
    package = package_hash.lookup(package_id)
    package.set_address(address, city, state, zipcode)
    print(f'Package {package_id} address corrected to {address} {city}, {state} {zipcode}')


if __name__ == '__main__':
    total_mileage = 0
    truck_one = truck.Truck()
    truck_two = truck.Truck([9, 5])
    truck_one_first_load = [14, 15, 16, 34, 26, 22, 24, 19, 20, 21, 1, 7, 29, 2, 33]
    truck_two_first_load = [31, 32, 25, 6, 36, 13,  39, 27, 35, 3, 8, 30, 5, 37, 38, 40]
    truck_one.load(truck_one_first_load)
    # get_delivered_packages()
    start_route(truck_one)
    total_mileage += truck_one.get_mileage()
    print('truck_one total mileage: ', truck_one.get_mileage())
    print('truck_one time: ', truck_one.get_time())

    truck_two.load(truck_two_first_load)
    start_route(truck_two)
    print('Truck_two total mileage: ', truck_two.get_mileage())
    print('Truck_two time:', truck_two.get_time())
    print(total_mileage)
    # correct address error
    print('Correct package #9 address error')
    correct_address(9, '410 S State St', 'Salt Lake City', 'UT', '84111')
    # get_delivered_packages()
    truck_two_second_load = [9, 10, 28, 18, 23, 11, 12, 4, 17]
    truck_two.load(truck_two_second_load)
    start_route(truck_two)
    print('Truck_two total mileage: ', truck_two.get_mileage())
    print('Truck_two time:', truck_two.get_time())
    total_mileage += truck_two.get_mileage()
    print(total_mileage)

    # while loop to let user see when packages have been delivered
    while True:
        response_str = input('Would you like to check when packages have been delivered? Enter Y or N ')
        response = response_str.lower()
        if response == 'n':
            print('Have a nice day, logging you out')
            break
        else:
            get_delivered_packages()



    # test to see what packages have been delivered by 9:30AM and delivered packages overall
    # package_hash.print_delivered_by(9, 30)
    # print('*****' * 4)
    # print('Packages delivered by 10:30:')
    # package_hash.print_delivered_by(10, 30)


