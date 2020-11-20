import unittest

from treeSerializer.serializer import Node, serialize, deserialize


class MyTestCase(unittest.TestCase):
    def test_deserialization(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    unittest.main()
