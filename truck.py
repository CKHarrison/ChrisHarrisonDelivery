from package import Package, create_package_table
from distance_matrix import create_distance_table, find_distance


class Truck:
    def __init__(self, package_id_list):
        self.package_id_list = package_id_list
        self.total_mileage = 0
        self.speed = 18
