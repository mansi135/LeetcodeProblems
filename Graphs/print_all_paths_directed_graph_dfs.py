"""Print all possible paths from source to destination in a Directed Graph"""

from collections import defaultdict


class DirectedGraph(object):

    def __init__(self):
        self.graph = defaultdict(list)
        self._all_paths = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths(self, s, d):

        visited = set()
        one_path = []

        self.dfs(s, d, visited, one_path)

        return self._all_paths

    def dfs(self, s, d, visited, one_path):

        if s in visited:
            return

        visited.add(s)
        one_path.append(s)

        if s == d:
            path = one_path[:]
            self._all_paths.append(path)

        if s in self.graph:
            for child in self.graph[s]:
                self.dfs(child, d, visited, one_path)

        visited.remove(s)
        one_path.pop()


def main():
    my_graph = DirectedGraph()

    my_graph.add_edge(2, 0)
    my_graph.add_edge(2, 1)
    my_graph.add_edge(0, 2)
    my_graph.add_edge(0, 1)
    my_graph.add_edge(0, 3)
    my_graph.add_edge(1, 3)


    print(my_graph.print_all_paths(2, 3))

main()