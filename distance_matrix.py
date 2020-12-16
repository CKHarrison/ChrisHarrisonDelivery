import csv
from package import create_package_table, lookup

package_hash = create_package_table()


def create_distance_table():
    distance_table_matrix = []

    with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
        distance_table_file = csv.reader(csv_file, delimiter=',')
        for row in distance_table_file:
            distance_table_matrix.append(row[1:-1])
    return distance_table_matrix


distance_table = create_distance_table()


# works
def find_distance_from_hub(package_id):
    """similar to find_distance_package, except this function just finds
     the distance from the hub and a package"""
    try:
        package_address = lookup(package_id)
        package_address_index = None
        for row in distance_table:
            if package_address in row:
                package_address_index = distance_table.index(row)
                break
        # return the distance from the hub to whatever location
        return float(distance_table[package_address_index][1])
    except Exception as e:
        print(f'there was an error: {e} -- for package id: {package_id}')
        print(package_address)


# works
def find_distance_between_packages(package_one, package_two):
    """Function takes the distance between the start address and end address
       and returns the distance between the two
    """
    start_address = lookup(package_one)
    end_address = lookup(package_two)
    # address_one and address_two holds index location of each address
    # now need to use that index as column to compare distances
    for row in distance_table:
        if start_address in row:
            address_one = distance_table.index(row)
            # print(f'address: {start_address}')
            # print('printing address_one index: ', address_one)
        if end_address in row:
            # print(f'address: {end_address}')
            address_two = distance_table.index(row)
            # print('printing address_two index: ', address_two)
    # use whichever address index is bigger, because that will have all the address info needed
    if address_one and address_two:
        calculate_address = max(address_one, address_two)
        # need to add one to account for name of address being the first column
        address_column = min(address_one, address_two) + 1
        return float(distance_table[calculate_address][address_column])
    else:
        return None


# currently works, might need to make changes, need to make sure to mark packages as delivered when destination reached
def find_shortest_route(id_list, current_package=None):
    """This function will find the shortest route among a list of packages and return the next destination to go to
    takes id list and optional package parameter, if second parameter is not supplied, it is assumed
    the starting address is the HUB location
    """
    # filtered list that contains packages that still need to be delivered
    non_delivered_packages = find_non_delivered_packages(id_list)

    # if the route is starting out from the HUB
    if current_package is None:
        current_address = float(distance_table[0][1])  # hub location
        shortest_distance = 100
        for package_id in non_delivered_packages:
            distance = find_distance_from_hub(package_id)
            if distance < shortest_distance:
                shortest_distance = distance
        return shortest_distance

    # find shortest route between all non delivered packages
    shortest_distance = 100
    for i in non_delivered_packages:
        # compare each package with each other package, does not compare previously compared packages
        if i < len(non_delivered_packages):
            for j in non_delivered_packages[i:]:
                print(f'testing between packages {i} and {j}')
                distance = find_distance_between_packages(i,j)
                if distance < shortest_distance:
                    shortest_distance = distance
                    print(f'current shortest distance is: {shortest_distance}')
    print(shortest_distance)


# works
def find_non_delivered_packages(id_list):
    """Takes in a list of package ids and returns a list of all packages that were not delivered"""
    non_delivered_packages = []
    for package_id in id_list:
        package = package_hash.get(package_id)
        if package.get_status() != 'delivered':
            non_delivered_packages.append(package_id)
    return non_delivered_packages


def find_shortest_distance_truck(id_list, truck_address):
    """This function takes the truck's current address and returns the next shortest distance
    and the address as a tuple"""
    # grab the address of the truck and return that column
    for row in distance_table:
        if truck_address in row:
            truck_address_index = distance_table.index(row)
            break


    shortest_distance = 100
    # look up package address in id list
    for package in id_list:
        package_address = lookup(package)
        # check to see if that address is in distance table
        for row in distance_table:
            # find column number of address
            if package_address in row:
                package_address_index = distance_table.index(row)
                # since the matrix is only half filled in must check to see which address comes after the other
                if package_address_index > truck_address_index:
                    # print('Distance is ', distance_table[package_address_index][truck_address_index + 1])
                    if float(distance_table[package_address_index][truck_address_index + 1]) < shortest_distance:
                        shortest_distance = float(distance_table[package_address_index][truck_address_index + 1])
                        # print('printing shortest distance: ', shortest_distance)
                        new_truck_address = distance_table[package_address_index][0]
                else:
                    if float(distance_table[truck_address_index][package_address_index + 1]) < shortest_distance:
                        shortest_distance = float(distance_table[truck_address_index][package_address_index + 1])
                        # print('printing shortest distance: ', shortest_distance)
                        new_truck_address = distance_table[package_address_index][0]
    # return a tuple with the shortest distance and the new address the truck will be at
    return shortest_distance, new_truck_address


def return_to_hub(truck_address):
    """This function returns the mileage when the truck goes back from it's current location to the hub"""
    for row in distance_table:
        if truck_address in row:
            truck_address_index = distance_table.index(row)

    distance_to_hub = distance_table[truck_address_index][1]
    return distance_to_hub, distance_table[0][0]



