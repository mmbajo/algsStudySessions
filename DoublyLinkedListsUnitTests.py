import DoublyLinkedLists as dll
import unittest

class Node(dll.Node):
    pass

# Helper Function for testing empty linked list
# Note that a non-empty linked list has its head and tail not equal to None
def expectEmpty(self, linkedList):
    self.assertEqual(linkedList.head, None)
    self.assertEqual(linkedList.tail, None)

# Helper Funtion for testing head and tail of a linked list
def expectHeadTail(self, linkedList, head, tail):
    self.assertEqual(linkedList.head, head)
    self.assertEqual(linkedList.tail, tail)

# Helper Function for testing a linked list with only one single Node!
def expectSingleNode(self, linkedList, node):
    self.assertEqual(linkedList.head, node)
    self.assertEqual(linkedList.tail, node)

# Helper Function for getting all nodes in a linked list to an array
def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values

# Helper Function for removing nodes
def removeNodes(linkedList, nodes):
    for node in nodes:
        linkedList.remove(node)

# Unit test class
class TestDoublyLilnkedList(unittest.TestCase):
    def test_case_1(self):
        linkedList = dll.DoublyLinkedList()
        node = Node(1)

        linkedList.setHead(node)
        expectSingleNode(self, linkedList, node)
        linkedList.removeNode(node)
        expectEmpty(self, linkedList)
        linkedList.setTail(node)
        expectSingleNode(self, linkedList, node)
        linkedList.removeWithNodesValue(1)
        expectEmpty(self, linkedList)
        linkedList.insertAtPosition(1, node)
        expectSingleNode(self, linkedList, node)

    def test_case_2(self):
        linkedList = dll.DoublyLinkedList()
        

if __name__ == '__main__':
    unittest.main()