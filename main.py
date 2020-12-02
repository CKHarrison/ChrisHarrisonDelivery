from package import Package, create_package_table
import csv

# Create distance table 2-D array
distance_table = []

with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
    distance_table_file = csv.reader(csv_file, delimiter=',')
    for row in distance_table_file:

        distance_table.append(row[:-1])


if __name__ == '__main__':
    package_hash = create_package_table()
    print(package_hash.print())
    print(distance_table)
