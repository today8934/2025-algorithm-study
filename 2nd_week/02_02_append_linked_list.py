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

    def get_node(self, index):
        node = self.head
        number = 0
        while(True):
            if (node == None): return "Out of Index"
            if (number == index):
                return node.data
            node = node.next
            number = number + 1

    def add_node(self, data, index):
        if (index < 0): return "Out of Index"
        if (index == 0):
            tmp_node = self.head
            self.head = Node(data)
            self.head.next = tmp_node
            return
        node = self.head
        number = 0
        while(True):
            if (node == None): return "Out of Index"
            if (number == index - 1):
                tmp_node = node.next
                node.next = Node(data)
                node.next.next = tmp_node
                return
            node = node.next
            number = number + 1

linked_list = LinkedList(5)

linked_list.append(3)
linked_list.append(4)
linked_list.append(12)

linked_list.print_all()
print(linked_list.get_node(4))
linked_list.add_node(7, 5)
linked_list.print_all()


    