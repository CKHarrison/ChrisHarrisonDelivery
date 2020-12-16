from package import create_package_table
from distance_matrix import find_shortest_distance_truck
import truck

def start_route(car):
    # if truck has early packages deliver them first
    if len(car.get_early_packages()):
        while car.get_early_packages():
            # find the shortest route to package
            distance, location = find_shortest_distance_truck(car.get_early_packages(), car.get_address())
            print(f'next distance is {distance} and next location: {location}')
            car.move(distance, location)
            print(car.get_early_packages())
            car.deliver_package(car.get_early_packages())
            print('delivered packages:', car.get_delivered_packages_list())
            print('early packages after delivered: ', car.get_early_packages())
            print('Current Address: ', car.get_address())


if __name__ == '__main__':
    package_hash = create_package_table()
    print('hello world')
    truck_one = truck.Truck()
    truck_two = truck.Truck([9,5])
    truck_one_first_load = [14, 15, 16, 34, 26, 22, 24, 19, 20, 21, 1, 7, 29, 2, 33]
    truck_one.load(truck_one_first_load)
    start_route(truck_one)
