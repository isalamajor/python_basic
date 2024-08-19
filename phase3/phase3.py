from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        visited = {}
        distances = {}  # Will store the distance from A to each vertex
        for v in self._vertices.keys():
            visited[v] = False
            distances[v] = None
        distances[start], visited[start] = 0, True
        visited_vertices = 1
        while visited_vertices != len(self._vertices):  # Mientras no todos hayan sido visitados
            for v1 in self._vertices.keys():  # I will find out for each vertex how to reach it from A
                for v2 in visited:
                    if visited[v2] and v2 != v1:
                        for adjvertex in self._vertices[v2]:
                            if v1 == adjvertex.vertex:  # If v2 -> v1
                                if visited[v1]:
                                    if distances[v1] > distances[v2] + 1:
                                        distances[v1] = distances[v2] + 1
                                if not visited[v1]:
                                    distances[v1] = distances[v2] + 1
                                    visited[v1] = True
                                    visited_vertices += 1

        return distances[end] if distances[end] is not None else 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if not self._directed:
            return self

        graphT = Graph(self._vertices.keys())  # We create the Transpose Graph, initially without any vertex

        # For each vertex, we check if it is in the Adjacency List of the rest of vertices.
        # If so, we connect that last vertex with the initial vertex we were working with.
        for v1 in self._vertices.keys():
            for v2 in self._vertices.keys():
                for adjvertex in self._vertices[v2]:
                    if adjvertex.vertex == v1:  # If v2 is connected towards v1
                        graphT.add_edge(v1, v2, adjvertex.weight)  # From v2 -> v1 to v1 -> v2
        return graphT

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for v1 in self._vertices.keys():
            # "reachable" is a list that stores the vertices that can be reached from v1, including v1:
            reachable = [v1]
            for v2 in self._vertices[v1]:
                if v2.vertex not in reachable:
                    reachable.append(v2.vertex)

            # This is to also include the vertices that can be reached from the vertices adjacent to v1:
            for v2 in reachable:
                for v3 in self._vertices[v2]:
                    if v3.vertex not in reachable:
                        reachable.append(v3.vertex)

            # If not every vertex in the graph can be reached from v1, we will return False
            if len(reachable) != len(self._vertices.keys()):
                return False
        return True  # Other ways, we return True
