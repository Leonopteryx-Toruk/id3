class Node:

    def __init__(self, column=None, value=None, classification=None):
        self.column = column
        self.value = value
        self.classification = classification
        self.children = []
        self.parent = None

    def node_to_str(self):
        node_str = "{column} = {value}".format(column=self.column, value=self.value)
        if self.classification is not None:
            node_str += ": {classification}".format(classification=self.classification)
        return node_str

    def add_child(self, node):
        self.children.append(node)

    def is_root(self):
        if self.parent is None:
            return True
        return False

    def set_parent(self, parent):
        self.parent = parent

    def get_column(self):
        return self.column

    def get_value(self):
        return self.value

    def get_classification(self):
        return self.classification

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

def tree_to_str(node, tree_str="", level=0):
    if not node.is_root():
        tree_str += node.node_to_str()
    # print("tree_str", tree_str)
    children = node.get_children()
    for i in range(len(children)):
        child = children[i]
        tree_str += "\n"
        for i in range(level):
            tree_str += "|\t"
        level_up = level+1
        tree_str = tree_to_str(child, tree_str, level=level_up)
    return tree_str

def print_tree(root):
    if not isinstance(root, Node):
        raise ValueError("root is not a node")
    root_str = tree_to_str(root)
    print(root_str)