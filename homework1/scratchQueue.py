class Queue:

	class Node:
		def __init__(self, item):
			self.item = item
			self.next = None

	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def peek(self):
		if self.is_empty():
			raise ValueError, "The Queue was Empty!"
		return self.head.item

	def add(self, item):
		if self.is_empty():
			self.head = Queue.Node(item)
			self.tail = self.head
		else:
			self.tail.next = Queue.Node(item)
			self.tail = self.tail.next
		self.size += 1

	def remove(self):
		result = self.peek()
		self.head = self.head.next
		self.size -= 1
		if self.is_empty():
			self.tail = None
		return result

	def is_empty(self):
		return self.size == 0

	def __str__(self):
		result = "["
		current = self.head
		while current is not None:
			if current is not self.head:
				result += ", " + str(current.item)
			else:
				result += str(current.item)
			current = current.next

		result += "]"
		return result

""" q.queue() -> return q.head.item
    q.remove() -> q.head = q.head.next()
    q.is_empty() -> q.head is not None
    q.add() ->
"""


q = Queue()
q.add(5)
q.add(10)
q.add(15)
q.remove()
print q