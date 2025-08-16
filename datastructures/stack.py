class Stack:
    def __init__(self):
        self.items = []  #list to hold stack elements

    def push(self, item):
        self.items.append(item)  #add item to top of stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  #remove and return top item
        return None  #return none if stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  #return top item without removing it
        return None  #return none if stack is empty

    def is_empty(self):
        return len(self.items) == 0  #check if stack is empty

    def size(self):
        return len(self.items)  #return number of items in stack
