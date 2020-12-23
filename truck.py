from datetime import datetime, timedelta
from distance_matrix import package_hash


class Truck:
    """Truck class that is responsible for grabbing the packages from the hub and delivering them across town
     Each truck has its own time that it keeps track of, and each truck has its list of packages, separated into two
     lists early deliveries and end of day deliveries."""

    def __init__(self, name, clock=None):
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
        self.name = name

    # create a deliver method which sets the package to delivered and sets the time they were delivered at
    def deliver_package(self, packages):
        """This function looks through the list of packages, gets the id of that package, and if the package matches
           the current address of the truck, it marks it as delivered, and removes that package from the list of
           packages the truck is carrying. This operates in Big O(N) time, as it only loops through the list of packages
           the truck is carrying"""
        for package_id in packages:
            package = package_hash.lookup(package_id)
            # have to format package address because
            package_address = package.get_address()[0] + f'({package.get_address()[-1]})'
            if package_address == self.truck_address:
                package.set_delivered(self.clock)
                self.delivered_packages_list.append(package_id)
                if package_id in self.early_packages:
                    self.early_packages.remove(package_id)
                else:
                    self.eod_packages.remove(package_id)

        # this last chunk of code is responsible for showing the packages status at various points in the day as per
        # section G of the rubric. Shows the full list at 9AM 10:07AM and 12:30PM
        nine_am = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                           hour=9, minute=00)
        nine_one = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                            hour=9, minute=1)
        ten_am = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                          hour=10, minute=00)
        ten_five = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                            hour=10, minute=8)
        twelve_thirty = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                 hour=12, minute=30)
        twelve_thirty_two = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                     hour=12, minute=32)

        if nine_am <= self.get_time() <= nine_one:
            print(f'******** printing package status at {self.get_time()} ********')
            package_hash.print_status()
            print(f'******** end package status ********')

        if ten_am <= self.get_time() <= ten_five:
            print(f'******** printing package status at {self.get_time()} ********')
            package_hash.print_status()
            print(f'******** end package status ********')

        if twelve_thirty <= self.get_time() <= twelve_thirty_two:
            print(f'******** printing package status at {self.get_time()} ********')
            package_hash.print_status()
            print(f'******** end package status ********')

    def _add_time(self, seconds):
        """"add time to the internal clock"""""
        self.clock += timedelta(seconds=seconds)

    def calculate_time(self, distance):
        """this function calculates the amount of time it takes for the truck to reach its destination
        then adds that time to the truck clock, Big O(1) runtime"""
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
        and the other for deliveries that are marked end of day. Big O(N) runtime complexity"""
        # set all packages delivery status to en route
        for package_id in list_of_packages:
            package = package_hash.lookup(package_id)
            package.set_en_route()

        for package_id in list_of_packages:
            package = package_hash.lookup(package_id)
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

    def compare_time(self, first_hour, first_minute, second_hour, second_minute):
        """Check to see if a certain time is between user set times. Big O(1) runtime"""
        first_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                              hour=first_hour, minute=first_minute)
        second_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                               hour=second_hour, minute=second_minute)

        if first_time >= self.get_time() <= second_time:
            return True
