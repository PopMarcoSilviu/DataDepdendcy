from enum import Enum


class Color(Enum):
    RED = '#FF0000'
    GREEN = '#00FF00'


class Node:

    def __init__(self, number, instruction, father=None):
        self.number = number
        self.instruction = instruction
        self.color = Color.GREEN
        self.father = father
        self.children = []
        self.nb_of_parents = 0
        self.time_left = 5

    def change_color(self):
        self.color = Color.GREEN if self.color != Color.GREEN else Color.RED

    def add_child(self, child):
        self.children.append(child)

    def add_father(self, father):
        self.father = father

    def delete_father(self):
        self.father = None

    def inc_parent_counter(self):
        self.nb_of_parents += 1

    def dec_parent_counter(self):
        self.nb_of_parents -= 1

    def __del__(self):
        print('Node ' + str(self.number) + ' destructed')

    def __str__(self):
        return str(self.instruction)

    def __repr__(self):
        return self.__str__()


def change_color_node_t(root, node):
    if root is None:
        return

    if root.number == node.number:
        for child in root.children:
            child.change_color()
        return

    for child in root.children:
        change_color_node_t(child, node)


class Graph:

    def __init__(self, node_list):
        self.nodes = []
        if isinstance(node_list, list):
            self.nodes.extend(node_list)
        else:
            self.nodes.append(node_list)

    def add_node(self, node):
        self.nodes.append(node)

    def change_color_node_children(self, node):
        for root in self.nodes:
            change_color_node_t(root, node)

    def get_size_tree(self, root):
        if root is None:
            return 0
        nb_of_nodes = 0

        for child in root.children:
            nb_of_nodes += self.get_size_tree(child)

        return 1 + nb_of_nodes

    def get_size(self):

        nb_of_nodes = 0

        for root in self.nodes:
            nb_of_nodes += self.get_size_tree(root)

        return nb_of_nodes

    def get_node_list(self):
        list_of_nodes = []

        for root in self.nodes:
            self.get_node_list_tree(root, list_of_nodes)

        list_of_nodes.sort(key=lambda x: x.number)
        return list_of_nodes

    def get_node_list_tree(self, root, list_of_nodes):
        if root is None:
            return

        list_of_nodes.append(root)

        for child in root.children:
            self.get_node_list_tree(child, list_of_nodes)

    def __str__(self):
        s = self.get_node_list()
        output = ''

        for x in s:
            output += str(x.number) + ' ' + str(x.color) + '   '
        return output


class LimitedQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def __getitem__(self, key):
        return self.queue[key]

    def dequeue(self):
        try:
            return self.queue.pop(0)
        except ValueError:
            pass

    def enqueue(self, element):
        self.queue.append(element)

        if len(self.queue) > self.max_size:
            self.dequeue()

    def enqueue_if_space(self, element):
        if len(self.queue) == self.max_size:
            return False

        self.queue.append(element)
        return True

    def get_size(self):
        return len(self.queue)
