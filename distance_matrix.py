import csv
from package import create_package_table, lookup

package_hash = create_package_table()
distance_table = []

with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
    distance_table_file = csv.reader(csv_file, delimiter=',')
    for row in distance_table_file:
        distance_table.append(row[1:-1])

print('*' * 4, 'distance table', '*' * 4)
print(distance_table)
print('*' * 16)

def find_distance(package_one, package_two):
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
            print(f'address: {start_address}')
            print('printing address_one index: ', address_one)
        if end_address in row:
            print(f'address: {end_address}')
            address_two = distance_table.index(row)
            print('printing address_two index: ', address_two)
    # use whichever address index is bigger, because that will have all the address info needed
    if address_one and address_two:
        calculate_address = max(address_one, address_two)
        # need to add one to account for name of address being the first column
        address_column = min(address_one, address_two) + 1
        return float(distance_table[calculate_address][address_column])
    else:
        return -1

print(find_distance(4, 20))
