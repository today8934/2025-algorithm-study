class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.current = self.head
    
    def append(self, value):
        new_node = Node(value)
        self.current.next = new_node
        self.current = new_node
    
    def print_all(self):
        node = self.head
        while(True):
            print(node.data)
            if (node.next == None): break
            node = node.next

linked_list = LinkedList(5)

linked_list.append(3)
linked_list.append(4)
linked_list.append(12)

linked_list.print_all()


    