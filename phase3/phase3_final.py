from graph import AdjacentVertex
from graph import Graph
import copy
import sys

class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if start == end:
            return 0

        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        distance = {}
        for v in self._vertices.keys():
            distance[v] = None

        # distance from start to start is 0
        distance[start] = 0

        i = 0
        while i <= len(self._vertices):
            # selects the node with minimum distance and not visited -> main
            min_ = sys.maxsize
            for v in self._vertices.keys():
                if visited[v] is False and distance[v] is not None and distance[v] <= min_:
                    min_ = distance[v]  # update the new smallest
                    main = v  # update the index of the smallest

            if main == end:
                i = len(self._vertices)
            else:
                visited[main] = True

                for adj in self._vertices[main]:
                    v = adj.vertex
                    # If current distance is bigger than distance from main
                    if visited[v] is False and (distance[v] is None or distance[v] > distance[main] + 1):
                        distance[v] = distance[main] + 1
            i += 1

        return distance[end] if distance[end] is not None else 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if not self._directed:
            return copy.deepcopy(self)

        graphT = Graph2(self._vertices.keys())  # We create the Transpose Graph, initially without any vertex

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


