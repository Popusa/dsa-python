from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.insert(0,val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return  len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

