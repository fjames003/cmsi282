from queue import *

q = Queue()

q.add(5)
q.add(True)
q.add('dog')
q.add({'x': 1, 'y': 2})
q.add(5.3)
q.remove()
q.remove()
print q.size()
print q.is_empty()