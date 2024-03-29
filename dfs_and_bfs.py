class Stack:
    def __init__(self):
        self.storage = []

    def add(self, node):
        self.storage.append(node)

    def contains(self, state):
        return any(node.state == state for node in self.storage)

    def empty(self):
        return len(self.storage) == 0

    def remove(self):
        if self.empty():
            raise Exception("Stack is empty")
        else:
            node = self.storage.pop()
            return node


class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception("Queue is empty")
        else:
            node = self.storage.pop(0)
            return node


class Node:
    def __init__(self, head, edge):
        self.edge = edge
        self.head = head
        self.tail = []

    def add_tail(self, tail):
        self.tail.append(tail)


point_a = Node(None, 'A')
point_b = Node(point_a, 'B')
point_c = Node(point_a, 'C')
point_d = Node(point_b, 'D')
point_e = Node(point_c, 'E')
point_f = Node(point_a, 'F')

point_a.add_tail(point_b)
point_a.add_tail(point_c)
point_a.add_tail(point_f)
point_b.add_tail(point_d)
point_c.add_tail(point_e)

initial_point = point_a
final_point = point_d


def dfs():
    frontier = Stack()
    global initial_point
    global final_point
    frontier.add(initial_point)

    explored_set = []
    actions = []

    while True:
        node = frontier.remove()
        explored_set.append(node)
        if node.edge == final_point.edge:
            while node.head is not None:
                actions.append(node)
                node = node.head
            actions.append(initial_point)
            actions.reverse()
            return actions, explored_set
        for tail in node.tail:
            if tail not in explored_set and tail not in frontier.storage:
                frontier.add(tail)


[actual_path, explored] = dfs()

print("Optimal path: ")

for path in actual_path:
    print(path.edge)

print("Explored set: ")

for path in explored:
    print(path.edge)
