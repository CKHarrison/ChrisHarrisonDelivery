class Vertex:
    # id is the the identifier of the vertex, in this case an address
    # connected_to list is a dictionary that shows all the vertices a particular vertex is connected with
    def __init__(self, address):
        self.id = address
        self.connected_with = {}

        # adds a neighbor that is connected to this vertex with a default weight of zero that can be adjusted
    def add_neighbor(self, neighbor, weight=0):
        self.connected_with[neighbor] = weight

    # returning a string format of the vertex
    def __str__(self):
        return str(self.id) + 'is connected with ' + str([v.id for v in self.connected_with])

    # returning the neighbors that this vertex is connected with
    def get_neighbors(self):
        return self.connected_with.keys()

    def get_id(self):
        return self.id

    def get_weight(self,neighbor):
        return self.connected_with[neighbor]


#
class Graph:
    """Graph class which implements the vertex class, allows the creation of a full undirected weighted graph"""
    def __init__(self):
        self.vertex_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, address):
        self.num_of_vertices += 1
        vertex = Vertex(address)
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
        return self.vertex_list.keys()
