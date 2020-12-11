import csv
from package import create_package_table, lookup


class Vertex:
    # id is the the identifier of the vertex, in this case an address
    # connected_to list is a dictionary that shows all the vertices a particular vertex is connected with
    def __init__(self, address):
        self.id = address.strip()
        self.connected_with = {}

        # adds a neighbor that is connected to this vertex with a default weight of zero that can be adjusted

    def add_neighbor(self, neighbor, weight=0):
        self.connected_with[neighbor] = weight

    # returning a string format of the vertex
    def __str__(self):
        return str(self.id) + ' is connected with ' + str([v.id for v in self.connected_with])

    # returning the neighbors that this vertex is connected with
    def get_neighbors(self):
        return self.connected_with.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_with[neighbor]


class Graph:
    """Graph class which implements the vertex class, allows the creation of a full undirected weighted graph"""

    def __init__(self):
        self.vertex_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, address):
        self.num_of_vertices += 1
        vertex = Vertex(address.strip())
        self.vertex_list[address] = vertex
        return vertex

    # get the vertex if in list otherwise return None to indicate it doesn't exist
    def get_vertex(self, vertex):
        if vertex in self.vertex_list:
            return self.vertex_list[vertex]
        return None

    # creating contain method to see if vertex is "in" graph
    def __contains__(self, item):
        return item in self.vertex_list

    # create iteration function so the graph can be iterated through if necessary
    def __iter__(self):
        return iter(self.vertex_list.values())

    def add_edge(self, from_v, to_v, weight=0):
        # checking to see if the vertex exists
        if from_v not in self.vertex_list:
            new_vertex = self.add_vertex(from_v)
        if to_v not in self.vertex_list:
            new_vertex = self.add_vertex(to_v)
        # if it exists, add edge
        self.vertex_list[from_v].add_neighbor(self.vertex_list[to_v], weight)

    # return all the vertices in the graph by showing the keys of vertex_list
    def get_vertices(self):
        return list(self.vertex_list.keys())


distance_graph = Graph()
distance_table_addresses = []
distance_table_mileage = []
distance_table = []

with open('distance_table.csv', encoding='utf-8-sig', newline='') as csv_file:
    distance_table_file = csv.reader(csv_file, delimiter=',')
    for row in distance_table_file:
        distance_table_addresses.append(row[: 2])
        distance_table_mileage.append(row[2:-1])
        distance_table.append(row[1:-1])

# for index, row in enumerate(distance_table_mileage):
#     # this gets the address from the corresponding cell in the address table and create new vertex
#     from_vertex_address = distance_table_addresses[index][1]
#     # add vertex
#     distance_graph.add_vertex(from_vertex_address)
#     # create edges for that vertex
#     if len(row) > 1:
#         for i in row[:-1]:
#             weight = float(i)
#             row_index = row.index(i)
#             to_address = distance_table_addresses[row_index][1]
#             distance_graph.add_edge(from_vertex_address, to_address, weight)


package_id_list = list(range(1, 17))


# Create generalized graph function which takes  a list of package ids, gets the addresses, and creates a graph
# from the addresses
def create_graph(id_list):
    new_graph = Graph()
    # iterate through package id list get each address, create vertex from address and add edges
    # create an address list from id_list
    address_list = [lookup(package_id) for package_id in id_list]
    print(address_list)
    for i in range(len(address_list)):
        # find the address from the list and create vertex, increment index every time
        from_vertex = address_list[i]
        new_graph.add_vertex(from_vertex)
    # loop through all of the vertices and connect the edges
    # for j in range(len(address_list)):
    #     new_graph.add_edge()

    # for index, row in enumerate(distance_table_mileage[id_list[0]], id_list[-1]):
    #     # this gets the address from the corresponding cell in the address table and create new vertex
    #     from_vertex_address = address_list[index]
    #     # add vertex
    #     new_graph.add_vertex(from_vertex_address)
    #     # create edges for that vertex
    #     if len(row) > 1:
    #         for i in row[:-1]:
    #             weight = float(i)
    #             row_index = row.index(i)
    #             to_address = distance_table_addresses[row_index][1]
    #             new_graph.add_edge(from_vertex_address, to_address, weight)

    # return new_graph
# print(create_graph(package_id_list))
# print('*' * 20)
# print('Distance table:')
# print(distance_table)
print(distance_table_mileage)

# print(distance_table_mileage)
# this works do not alter for now
# print(distance_graph.get_vertices())
