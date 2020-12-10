from package import Package, create_package_table
import csv

# Create distance table 2-D array
distance_table = []
package_hash = create_package_table()

with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
    distance_table_file = csv.reader(csv_file, delimiter=',')
    for row in distance_table_file:
        distance_table.append(row[:-1])


# Lookup function to get the address of the package and the corresponding address in distance table
def lookup(package_id):
    package = package_hash.get(package_id)
    package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
    for row in distance_table:
        if package_address in row[1].strip():
            return row
    # if address is not found return None
    return None


print(distance_table)
print(lookup(20))
