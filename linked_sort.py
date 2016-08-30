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

    def remove(self,data):
        node = self.head
        prev_node = None

        while node is not None:
            if node.data == data:
                prev_node.next = node.next
            prev_node = node
            node = node.next       
        

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
print "-----------------remove ----------------"
mylist.remove(2)
mylist.show()
print "-----------------add ----------------"
mylist.add(8)
mylist.show()
