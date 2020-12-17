from distance_matrix import find_shortest_distance_truck, package_hash, \
    return_to_hub, lookup, fix_address
import truck


def start_route(car):
    # if truck has early packages deliver them first
    if len(car.get_early_packages()):
        while len(car.get_early_packages()) > 0:
            # find the shortest route to package
            distance, location = find_shortest_distance_truck(car.get_early_packages(), car.get_address())
            # print(f'next distance is {distance} and next location: {location}')
            car.move(distance, location)

            # print(car.get_early_packages())
            car.deliver_package(car.get_early_packages())
            # print('delivered packages:', car.get_delivered_packages_list())
            # print('early packages after delivered: ', car.get_early_packages())
            # print('Current Address: ', car.get_address())
        print('Current time is ', car.get_time())
        print('current mileage is ', car.get_mileage())
        print('Delivered packages: ', car.get_delivered_packages_list())
        print('packages to be delivered:', car.get_eod_packages())
        print('current address is: ', car.get_address())

        # deliver rest of packages
        if len(car.get_eod_packages()):
            while len(car.get_eod_packages()) > 0:
                distance, location = find_shortest_distance_truck(car.get_eod_packages(), car.get_address())
                car.move(distance, location)
                car.deliver_package(car.get_eod_packages())
        print('Current time is ', car.get_time())
        print('current mileage is ', car.get_mileage())
        print('Delivered packages: ', car.get_delivered_packages_list())
        print('packages to be delivered:', car.get_eod_packages())
        distance_to_hub, current_location = return_to_hub(car.get_address())
        print('Returning to hub')
        car.move(distance_to_hub, current_location)
    else:
        while len(car.get_eod_packages()) > 0:
            distance, location = find_shortest_distance_truck(car.get_eod_packages(), car.get_address())
            car.move(distance, location)
            car.deliver_package(car.get_eod_packages())
    print('Current time is ', car.get_time())
    print('current mileage is ', car.get_mileage())
    print('Delivered packages: ', car.get_delivered_packages_list())
    print('packages to be delivered:', car.get_eod_packages())
    distance_to_hub, current_location = return_to_hub(car.get_address())
    print('Returning to hub')
    car.move(distance_to_hub, current_location)


# get packages delivered by a user specified time if none have been delivered, show current status
def get_delivered_packages():
    print('Please enter when you want to see packages delivered.')
    hour = int(input('Please enter hour, in form of 24 hour clock. i.e 9am is 09, 10pm is 22: '))
    minutes = int(input('Please enter minutes from 0 - 60:'))
    try:
        sorted(package_hash.print_delivered_by(hour, minutes))
    except Exception as e:
        print('No packages have been delivered yet, here are all current package status:')
        package_hash.print_status()


def correct_address(package_id, address, city, state, zipcode):
    package = package_hash.get(package_id)
    package.set_address(address, city, state, zipcode)
    print(f'Package {package_id} address corrected to {address} {city}, {state} {zipcode}')
    print(package_hash.get(9).get_address())


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
    # print('truck_one total mileage: ', truck_one.get_mileage())
    # print('truck_one time: ', truck_one.get_time())

    truck_two.load(truck_two_first_load)
    start_route(truck_two)
    print('Truck_two total mileage: ', truck_two.get_mileage())
    print('Truck_two time:', truck_two.get_time())
    print(total_mileage)
    # correct address error
    print('Correct package #9 address error')
    correct_address(9, '410 S State St', 'Salt Lake City', 'UT', '84111')
    print(package_hash.get(9))
    # get_delivered_packages()
    truck_two_second_load = [9, 10, 28, 18, 23, 11, 12, 4, 17]
    truck_two.load(truck_two_second_load)
    start_route(truck_two)
    print('Truck_two total mileage: ', truck_two.get_mileage())
    print('Truck_two time:', truck_two.get_time())
    total_mileage += truck_two.get_mileage()
    print(total_mileage)


    # test to see what packages have been delivered by 9:30AM and delivered packages overall
    # package_hash.print_delivered_by(9, 30)
    # get_delivered_packages()

