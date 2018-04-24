# My implementation of topological sort in a DAG

from collections import defaultdict

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)
        # self.graph = {}


    def add_edge(self, u, v):
        self.graph[u].append(v)

        # This copy is linear time O(n), used with self.graph = {}
        # self.graph[u] = self.graph.get(u, []) + [v]

        # so instead of above, use this so that we are not crearting a new list every time
        # if u not in self.graph:
        #     ulist = []
        #     self.graph[u] = ulist
        # else:
        #     ulist = self.graph[u]
        # ulist.append(v)

        # Wrong:
        # self.graph.setdefault(u, None)


    def topological_sort(self):

        visited = set()
        stack = []

        for node in self.graph.keys():  # check all nodes in graph
            self.sort_util(node, stack, visited)

        # print(stack)

        stack.reverse()
        return stack

    def sort_util(self, node, stack, visited):

        if node in visited:
            return

        visited.add(node)

        #now check adjacency list for each node in graph
        if node in self.graph:
            for child in self.graph[node]:
                self.sort_util(child, stack, visited)

        stack.append(node)


    # This method was checking node not in visited at two places:
    # def topological_sort(self):
    #
    #     print(self.graph)
    #
    #     visited = set()
    #     stack = []
    #
    #     for node in self.graph.keys():  # check all nodes in graph
    #         if node not in visited:
    #             self.sort_util(node, stack, visited)
    #
    #     print(stack)
    #
    #     stack.reverse()
    #     return stack
    #
    # def sort_util(self, node, stack, visited):
    #
    #     visited.add(node)
    #
    #     # now check adjacency list for each node in graph
    #     if node in self.graph:
    #         for child in self.graph[node]:
    #             if child not in visited:
    #                 self.sort_util(child, stack, visited)
    #
    #     stack.append(node)


def main():
    my_graph = Graph()

    my_graph.add_edge('A', 'C')
    my_graph.add_edge('B', 'C')
    my_graph.add_edge('B', 'E')
    my_graph.add_edge('C', 'D')
    my_graph.add_edge('D', 'F')
    my_graph.add_edge('E', 'F')
    my_graph.add_edge('F', 'G')

    print(my_graph.topological_sort())

main()