#print "linked List(Sorted)"
# don't change node's positions, just change data of node.
class Node(object):
    def __init__(self, data, next): # 
        self.data = data
        self.next = next

class LinkedList(object):

    head = None 
    tail = None 

    def add(self, data):
        tmpnode = None
        tmpdata = None
        new_node = Node(data, None)  
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            tmpnode = self.head
            while tmpnode is not None:
                if tmpnode.data > new_node.data:
                    tmpdata = new_node.data  
                    new_node.data = tmpnode.data 
                    tmpnode.data = tmpdata
                tmpnode = tmpnode.next
            self.tail = new_node

    def show(self):
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None



mylist = LinkedList()
mylist.add(5)
mylist.add(10)
mylist.add(7)
mylist.add(3)
mylist.add(1)
mylist.add(9)
mylist.add(2)
mylist.add(15)

mylist.show()
# output
# 1  ->  2  ->  3  ->  5  ->  7  ->  9  ->  10  ->  15  ->  None