import csv
from hashtable import HashTable


class Package:
    """
    Package class that stores the information of a package. Id, delivery address, weight,
     delivery time and any special notes which default to an empty string if there are none
    """

    def __init__(self, package_id, address, city, state, zipcode, delivery_time,
                 weight, special_notes=None, delivery_status="en route"):
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
        # delivery status for package defaults to en route only changes if delivered
        self.delivery_status = delivery_status

    # Get package id
    def get_package_id(self):
        return self.package_id

    # Get address which returns a list, each element is a part of the address
    def get_address(self):
        address_list = [self.address, self.city, self.state, self.zipcode]
        return address_list

    # Set new address for package, needed if there is an incorrect address
    def set_address(self, address, city,  state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

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

    # Get delivery status of package
    def get_status(self):
        return self.delivery_status

    # Set delivery status -- Changes if package is delivered
    def set_delivered(self):
        self.delivery_status = 'delivered'

    # Override method to return a string version of the package so the contents can be displayed nicely
    def __str__(self):
        return "ID: {}, address: {} {}, {}, {}, to be delivered at: {}. Weight: {}, special notes: {}, status: {}".format(
            self.package_id, self.address, self.city, self.state, self.zipcode, self.delivery_time, self.weight,
            self.special_notes, self.delivery_status)


def create_package_table():
    """
    This function creates the hashtable of packages and returns the hashtable.
    The purpose of this function is to compartmentalize the creation of the table,
    allowing for use in the main program
    without needing to delve behind the scenes.
    """
    # package_hashtable will store all of the packages
    package_hashtable = HashTable()
    # Each row is of length 8 if no special instructions, 9 if there are instructions
    with open('package_csv.csv', newline='') as csv_file:
        package_data = csv.reader(csv_file, delimiter=',')
        # Skip the header row and only read in package data
        next(package_data)
        # Create a new package based on each row of the package table will add special notes if available
        for row in package_data:
            package_id, address, city, state, zipcode, delivery_time, weight = row[:7]
            if len(row) == 9:
                notes = row[7]
                new_package = Package(package_id, address, city, state, zipcode, delivery_time, weight, notes)
                package_hashtable.add(new_package.get_package_id(), new_package)
            else:
                new_package = Package(package_id, address, city, state, zipcode, delivery_time, weight)
                package_hashtable.add(new_package.get_package_id(), new_package)
    return package_hashtable


# package lookup function which takes a package id and returns the package address
def lookup(package_id):
    try:
        package_hash = create_package_table()
        package = package_hash.get(package_id)
        package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
        if package_address:
            return package_address
    except:
        # if address is not found return None
        return None
