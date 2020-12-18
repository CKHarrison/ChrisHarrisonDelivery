import csv
from hashtable import HashTable


class Package:
    """
    Package class that stores the information of a package. Id, delivery address, weight,
     delivery time and any special notes which default to an empty string if there are none
    """

    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline,
                 weight, special_notes=None, delivery_status="at hub"):
        # Make sure package id is an integer
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        # casts weight into an integer
        self.weight = int(weight)
        self.special_notes = special_notes
        # delivery status for package defaults to en route only changes if delivered
        self.delivery_status = delivery_status
        # time of delivery
        self.time_delivered = None

    # Get package id
    def get_package_id(self):
        return self.package_id

    # Get address which returns a list, each element is a part of the address
    def get_address(self):
        address_list = [self.address, self.city, self.state, self.zipcode]
        return address_list

    # Set new address for package, needed if there is an incorrect address
    def set_address(self, address, city, state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # Get delivery deadline
    def get_delivery_deadline(self):
        return self.delivery_deadline

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
    def set_delivered(self, time):
        self.time_delivered = time
        self.delivery_status = f'delivered at {self.time_delivered}'

    # get time_delivered
    def get_time_delivered(self):
        return self.time_delivered

    # Sets package to en route status
    def set_en_route(self):
        self.delivery_status = 'en route'

    # Sets package to 'at hub' status
    def set_at_hub(self):
        self.delivery_status = 'at hub'

    # Override method to return a string version of the package so the contents can be displayed nicely
    def __str__(self):
        return "ID: {}, address: {} {}, {}, {}, to be delivered at: {}. Weight: {}, special notes: {}, status: {}," \
               " time delivered: {}".format(
            self.package_id, self.address, self.city, self.state, self.zipcode, self.delivery_deadline, self.weight,
            self.special_notes, self.delivery_status, self.time_delivered)


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
            package_id, address, city, state, zipcode, delivery_deadline, weight = row[:7]
            if len(row) == 9:
                notes = row[7]
                new_package = Package(package_id, address, city, state, zipcode, delivery_deadline, weight, notes)
                package_hashtable.insert(new_package.get_package_id(), new_package)
            else:
                new_package = Package(package_id, address, city, state, zipcode, delivery_deadline, weight)
                package_hashtable.insert(new_package.get_package_id(), new_package)
    return package_hashtable


# package lookup function which takes a package id and returns the package address
package_hash = create_package_table()


def lookup(package_id):
    try:
        package = package_hash.lookup(package_id)
        package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
        if package_address:
            return package_address
    except:
        # if address is not found return None
        return None


def lookup_alternate(package_id, address=None, city=None, deadline=None, zipcode=None, status=None):
    package = package_hash.lookup(package_id)
    if address is not None:
        package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
        if package_address:
            return package_address
    if city is not None:
        return package.get_address()[1]
    if deadline is not None:
        return package.get_delivery_deadline()
    if zipcode is not None:
        return package.get_address()[-1]
    if status is not None:
        return package.get_status()

