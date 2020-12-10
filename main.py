from package import Package, create_package_table
import csv

# Create distance table 2-D array
distance_table = []

with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
    distance_table_file = csv.reader(csv_file, delimiter=',')
    for row in distance_table_file:

        distance_table.append(row[:-1])
package_table = create_package_table()

if __name__ == '__main__':
    print('hello world')
    for row in distance_table:
        print(row)