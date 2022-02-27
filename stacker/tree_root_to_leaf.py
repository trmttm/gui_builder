class Node:
    def __init__(self, name):
        self.name = name
        self.previous_node = 'root'
        self.next_nodes = []

    def set_previous(self, previous):
        self.previous_node = previous

    def add_next(self, next_):
        self.next_nodes.append(next_)
