from queue import Queue
from stack import Stack
from priority_queue import PriorityQueue


class Graph:
    def __init__(self):
        self.__nodes = {}

    def add_node(self, node):
        name = node.name
        if self.__nodes.get(name):
            raise ValueError(f"`{name}` already in graph")
        self.__nodes[name] = node

    def bfs(self, start, stop):
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        visited = set()
        queue = Queue()
        queue.enqueue((0, self.__nodes[start]))  # [(distance, curr)]
        while len(queue) > 0:
            distance_traveled, curr = queue.dequeue()
            visited.add(curr)
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                queue.enqueue(
                    (distance_traveled + vertex.weight, vertex.target)
                )

        print("No path found")

    def dfs(self, start, stop):
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        visited = set()
        stack = Stack()
        stack.enqueue((0, self.__nodes[start]))  # [(distance, curr)]
        while len(stack) > 0:
            distance_traveled, curr = stack.dequeue()
            visited.add(curr)
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                stack.enqueue(
                    (distance_traveled + vertex.weight, vertex.target)
                )

        print("No path found")

    def djikstra(self, start, stop):
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        priority_queue = PriorityQueue(key=lambda x: x[0])
        priority_queue.enqueue(
            (0, self.__nodes[start], [])
        )  # [(distance, curr, visited)]
        while len(priority_queue) > 0:
            distance_traveled, curr, visited = priority_queue.dequeue()
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                priority_queue.enqueue(
                    (distance_traveled + vertex.weight, vertex.target, visited + [curr])
                )

        print("No path found")


class Node:
    def __init__(self, name):
        self.name = name
        self.vertices = []

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise ValueError(f"Can't add duplicate vertex to node `{self.name}`")
        self.vertices.append(vertex)


class Vertex:
    def __init__(self, target, weight=1):
        self.target = target
        self.weight = weight


if __name__ == "__main__":
    g = Graph()

    frankfurt = Node("Frankfurt")
    mannheim = Node("Mannheim")
    wurzburg = Node("Wurzburg")
    stuttgart = Node("Stuttgart")
    kassel = Node("Kassel")
    karlshure = Node("Karlshure")
    ertfurt = Node("Ertfurt")
    nurnberg = Node("Nurnberg")
    augsburg = Node("Augsburg")
    muenchen = Node("Muenchen")

    avaiable_paths = [
        (frankfurt, mannheim, 85),
        (frankfurt, wurzburg, 217),
        (frankfurt, kassel, 173),
        (mannheim, karlshure, 80),
        (karlshure, augsburg, 250),
        (augsburg, muenchen, 84),
        (wurzburg, ertfurt, 186),
        (wurzburg, nurnberg, 103),
        (nurnberg, stuttgart, 183),
        (nurnberg, muenchen, 167),
        (kassel, muenchen, 502),
    ]

    nodes = set()
    for node_a, node_b, distance in avaiable_paths:
        node_a.add_vertex(Vertex(node_b, distance))
        node_b.add_vertex(Vertex(node_a, distance))

        nodes.add(node_a)
        nodes.add(node_b)

    for node in nodes:
        # print(node.name)
        g.add_node(node)

    g.add_node(Node("Jakarta"))

    g.bfs("Frankfurt", "Stuttgart")
    g.dfs("Frankfurt", "Ertfurt")
    g.djikstra("Frankfurt", "Ertfurt")

    g.djikstra("Jakarta", "Muenchen")
