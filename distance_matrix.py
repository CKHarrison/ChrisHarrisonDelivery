import csv
from package import package_hash, lookup


def create_distance_table():
    distance_table_matrix = []

    with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
        distance_table_file = csv.reader(csv_file, delimiter=',')
        for row in distance_table_file:
            distance_table_matrix.append(row[1:-1])
    return distance_table_matrix


distance_table = create_distance_table()


def find_shortest_distance_truck(id_list, truck_address):
    """This function takes the truck's current address and returns the next shortest distance
    and the address as a tuple
    This is the main algorithm that the program uses, it is in itself a greedy algorithm that compares two addresses,
    the trucks and the packages in the truck and finds the next closest package. It always chooses the shortest route
    every time. It runs in Big O(n^2) time"""
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
                    if float(distance_table[package_address_index][truck_address_index + 1]) < shortest_distance:
                        shortest_distance = float(distance_table[package_address_index][truck_address_index + 1])
                        new_truck_address = distance_table[package_address_index][0]
                else:
                    if float(distance_table[truck_address_index][package_address_index + 1]) < shortest_distance:
                        shortest_distance = float(distance_table[truck_address_index][package_address_index + 1])
                        new_truck_address = distance_table[package_address_index][0]
    # return a tuple with the shortest distance and the new address the truck will be at
    return shortest_distance, new_truck_address


def return_to_hub(truck_address):
    """This function returns the mileage when the truck goes back from it's current location to the hub as a tuple
    this algorithm has a Big O(N) runtime complexity. As it linearly searches for the address on the distance table"""
    for row in distance_table:
        if truck_address in row:
            truck_address_index = distance_table.index(row)

    distance_to_hub = distance_table[truck_address_index][1]
    return float(distance_to_hub), distance_table[0][0]


