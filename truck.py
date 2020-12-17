from datetime import datetime, timedelta
from package import Package, create_package_table
from distance_matrix import package_hash




class Truck:
    # import date time library and use the time delta operation
    # class variable that holds the clock time
    # each truck has their own time update that status based on the distance travelled
    def __init__(self, clock=None):
        if clock is None:
            # set clock time to be initialized to 8:00 AM
            self.clock = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8)
        else:
            self.clock = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                  hour=clock[0], minute=clock[1])
        self.package_id_list = []
        self.early_packages = []
        self.eod_packages = []
        self.delivered_packages_list = []
        self.total_mileage = 0
        self.speed = 18
        self.truck_address = "HUB"  # starts out initially at the wgu hub

    # create a deliver method which sets the package to delivered and sets the time they were delivered at
    def deliver_package(self, packages):
        for package_id in packages:
            package = package_hash.get(package_id)
            # have to format package address because
            package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
            if package_address == self.truck_address:
                package.set_delivered(self.clock)
                print(f'package {package.get_package_id()} delivered at: {package.get_status()}')
                self.delivered_packages_list.append(package_id)
                if package_id in self.early_packages:
                    self.early_packages.remove(package_id)
                else:
                    self.eod_packages.remove(package_id)

    def _add_time(self, seconds):
        """"add time to the internal clock"""""
        self.clock += timedelta(seconds=seconds)

    def calculate_time(self, distance):
        """this function calculates the amount of time it takes for the truck to reach its destination
        then adds that time to the truck clock"""
        # calculate the speed in seconds .005 miles per second
        speed_in_seconds = 18 / 3600
        amount_of_seconds = distance / speed_in_seconds
        self._add_time(amount_of_seconds)

    def get_time(self):
        return self.clock

    # update truck address
    def _update_address(self, address):
        self.truck_address = address

    # get truck address
    def get_address(self):
        return self.truck_address

    # move truck and set new address
    def move(self, distance, address):
        self.calculate_time(distance)
        self._update_address(address)
        self.total_mileage += distance

    # load truck with packages
    def load(self, list_of_packages):
        """loads all the packages in the truck into two separate lists, one for early delivers,
        and the other for deliveries that are marked end of day"""
        # set all packages delivery status to en route
        for package_id in list_of_packages:
            package = package_hash.get(package_id)
            package.set_en_route()

        for package_id in list_of_packages:
            package = package_hash.get(package_id)
            if package.get_delivery_deadline() != "EOD":
                self.early_packages.append(package_id)
            else:
                self.eod_packages.append(package_id)

    def get_early_packages(self):
        return self.early_packages

    def get_eod_packages(self):
        return self.eod_packages

    def get_delivered_packages_list(self):
        return self.delivered_packages_list

    def get_mileage(self):
        return self.total_mileage

