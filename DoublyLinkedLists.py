class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.removeNode(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
            
    def insertAfter(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.removeNode(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        currPosition = 1
        currNode = self.head
        while currNode is not None and currPosition != position:
            currNode = currNode.next
            currPosition += 1
        if currNode is not None:
            self.insertBefore(currNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeWithNodesValue(self, value):
        currNode = self.head
        while currNode is not None:
            nodeToRemove = currNode
            currNode = currNode.next
            if nodeToRemove.value == value:
                self.removeNode(nodeToRemove)

    def removeNode(self, node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNode(self, value):
        currNode = self.head
        while currNode is not None and currNode.value != value:
            currNode = currNode.next
        return currNode is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
