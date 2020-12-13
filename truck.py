from package import Package, create_package_table
from distance_matrix import create_distance_table


class Truck:
    # import date time library and use the time delta operation
    # class variable that holds the clock time
    # each truck has their own time update that status based on the distance travelled
    def __init__(self, package_id_list):
        self.package_id_list = package_id_list
        self.total_mileage = 0
        self.speed = 18
        # set clock time to be initalized to 8:00 AM

    # Create a method called deliver early packages
    # takes all packages with special notes that have time to deliver before EOD
    # plugs them in first so they are delivered, after that all other packages are delivered

    # create method to get time of deliveries, this can be in the truck method or distance helper methods
