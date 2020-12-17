from package import create_package_table
from distance_matrix import find_shortest_distance_truck, package_hash, return_to_hub
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
        car.move(distance_to_hub, current_location)
if __name__ == '__main__':
    truck_one = truck.Truck()
    truck_two = truck.Truck([9,5])
    truck_one_first_load = [14, 15, 16, 34, 26, 22, 24, 19, 20, 21, 1, 7, 29, 2, 33]
    truck_one.load(truck_one_first_load)
    start_route(truck_one)
    print(truck_one.total_mileage)
    print(truck_one.get_time())

    # for p_id in truck_one_first_load:
    #     package = package_hash.get(p_id)
    #     print(package.get_status())
