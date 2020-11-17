import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    def serializer(node, parent, direction):
        string = f"{parent}{f'{direction}' if direction else ''} = {node.val}\n"
        parent = f"{parent}{direction}"
        if node.left:
            queue.append({"node": node.left, "parent": parent, "string": string, "direction": ".left"})
        if node.right:
            queue.append({"node": node.right, "parent": parent, "string": string, "direction": ".right"})

        return string

    string = ""
    queue = [{"node": node, "parent": node.val, "direction": ""}]

    while queue:
        try:
            for index, node_dict in enumerate(queue):
                queue.pop(index)
                string += serializer(node_dict["node"], parent=node_dict["parent"],
                                     direction=node_dict["direction"])
        except RuntimeError:
            continue

    return string


def deserialize(s: str):
    instructions = s.split("\n")
    root_name = re.findall("\w+\s=", instructions.pop(0))[0].replace(" =", "")
    root = Node(f"'{root_name}'")
    for instruction in instructions[:-1]:
        node, value = instruction.split(" = ")
        try:
            node_name, node_attr = node.split(sep=".")
        except ValueError:
            node_name, node_attr = re.findall("(?:\w+\.)+|\w+$", node)
            node_name = node_name.rstrip(".")
        node_name = node_name.replace(root_name, "root")
        setattr(eval(node_name), node_attr, Node(value))

    return root
