class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_univals(root: Node):
    def counter(node: Node):
        count = 0
        try:
            if node.left.val == node.right.val:
                count += 1
        except AttributeError:
            if node.left is None and node.right is None:
                count += 1

        for subnode in [node.left, node.right]:
            if subnode is not None:
                queue.append(subnode)

        return count

    univals = 0
    queue = [root]

    while queue:
        for index, node in enumerate(queue):
            queue.pop(index)
            univals += counter(node)

    return univals
