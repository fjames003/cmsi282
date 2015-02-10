class Node:
    
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None
        self.parent = None
        self.color = False
    
    def get_value(self):
        return self.value
        
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_color(self):
        return self.color

    def flip_color(self):
        self.color = not self.color