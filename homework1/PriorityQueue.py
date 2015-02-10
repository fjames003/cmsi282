class PriorityQueue:

    def __init__(self):
        self.heap = []

    def add(self, x):
        self.heap.append(x)
        self.sift_up(self.size() -1)
        return self

    def peek(self):
        if self.is_empty():
            raise ValueError, "The Queue was empty!"
        else:
            return self.heap[0]

    def remove(self):
        if self.is_empty():
            raise ValueError, "The Queue was empty!"
        elif self.size() == 1:
            self.heap.pop(0)
        else:
            self.heap.pop(0)
            self.sift_down(0)
        return self

    def sift_up(self, index):
        parent = (index - 1) // 2
        if parent < 0 or self.heap[index] > self.heap[parent]:
            return self
        else:
            _tempParent = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = _tempParent
            self.sift_up(parent)
            return self

    def sift_down(self, index):
        child = (index * 2) + 1
        if child > self.size() - 1:
            return self
        else:
            child = child + 1 if (child + 1 < self.size() - 1 and self.heap[child + 1] < self.heap[child]) else child
            if self.heap[child] < self.heap[index]:
                _tempChild = self.heap[child]
                self.heap[child] = self.heap[index]
                self.heap[index] = _tempChild
                self.sift_down(child)
            return self
            
    def is_empty(self):
        return self.size() == 0

    def heapify(self):
        pass

    def size(self):
        return len(self)
    
    def __len__(self):
        return len(self.heap)
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            result = "[" 
            for i in self.heap:
                result += str(i) + ", "
            result = result[:-2] + "]"
        return result