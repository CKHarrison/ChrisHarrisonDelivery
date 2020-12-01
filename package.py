import csv
from hashtable import HashTable


class Package:
    """
    Package class that stores the information of a package. Id, delivery address, weight,
     delivery time and any special notes which default to an empty string if there are none
    """

    def __init__(self, package_id, address, city, state, zipcode, delivery_time, weight, special_notes=None):
        # Make sure package id is an integer
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        # casts weight into an integer
        self.weight = int(weight)
        self.special_notes = special_notes

    # Get package id
    def get_package_id(self):
        return self.package_id

    # Get address which returns a list, each element is a part of the address
    def get_address(self):
        address_list = [self.address, self.city, self.state, self.zipcode]
        return address_list

    # Get delivery_time
    def get_delivery_time(self):
        return self.delivery_time

    # Get weight
    def get_weight(self):
        return self.weight

    # Get special notes if there are any, if not, return None
    def get_special_notes(self):
        if self.special_notes is not None:
            return self.special_notes
        return None

    # Override method to return a string version of the package
    def __str__(self):
        return "ID: {}, address: {} {}, {}, {}, to be delivered at: {}. Weight: {}, Special notes: {}".format(
            self.package_id, self.address, self.city, self.state, self.zipcode, self.delivery_time, self.weight,
            self.special_notes)


package_hashtable = HashTable()

# Each row is of length 8 if no special instructions, 9 if there are instructions
with open('package_csv.csv', newline='') as csv_file:
    package_data = csv.reader(csv_file, delimiter=',')
    # Skip the header row and only read in package data
    next(package_data)
    # Create a new package based on each row of the package table
    for row in package_data:
        id, address, city, state, zip, delivery_time, weight = row[:7]
        if len(row) == 9:
            notes = row[7]
            new_package = Package(id, address, city, state, zip, delivery_time, weight, notes)
            package_hashtable.add(new_package.get_package_id(), new_package)
        else:
            new_package = Package(id, address, city, state, zip, delivery_time, weight)
            package_hashtable.add(new_package.get_package_id(), new_package)


result = package_hashtable.print()
print(result)
# Distance table test
# with open('distance_table.csv', newline='') as distance_csv:
#     distance_table = csv.reader(distance_csv, delimiter=',')
#     for row in distance_table:
#         print(row)
