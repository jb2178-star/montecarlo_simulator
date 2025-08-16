class Queue: #not used yet
    def __init__(self):
        self.items = [] #list to store queue elements

    def enqueue(self, item):
        self.items.append(item) #add item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #remove from the front of the queue
        return None #return none if queue is empty

    def is_empty(self):
        return len(self.items) == 0 #check if queue is empty

    def size(self):
        return len(self.items) #return number of items in the queue
