class Node: #singulary linked list
    def __init__(self, data):
        self.data = data #store node's data
        self.next = None #pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None #start of the linked list

    def append(self, data):
        new_node = Node(data) #create a new node
        if not self.head:
            self.head = new_node #if list empty, set new node as head
            return
        last = self.head
        while last.next:
            last = last.next #traverse to the last node
        last.next = new_node #append new node at the end

    def to_list(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data) #collect node data into list
            current = current.next
        return elems

    def __str__(self):
        return "->".join(str(data) for data in self.to_list())   #string representation of list
    def remove_last(self):
        if not self.head:
            return None
        if not self.head.next:  # Only one node
            data = self.head.data
            self.head = None
            return data
        # Find second to last node
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data
    
