import unittest
from PriorityQueue import *

class TestQueue(unittest.TestCase):

	def test_new_queue_has_size_zero(self):
		p = PriorityQueue()
		self.assertEqual(p.size(), 0)

	def test_is_empty_for_new_queue_is_true(self):
		p = PriorityQueue()
		self.assertTrue(p.is_empty())

	def test_we_can_add_five_elements(self):
		p = PriorityQueue()
		p.add(10)
		p.add(20)
		p.add(30)
		p.add(40)
		p.add(50)
		self.assertTrue(p.size(), 5)
		self.assertTrue(p.peek(), 10)

	def test_for_priority_removal(self):
		p = PriorityQueue()
		p.add(10)
		p.add(20)
		p.add(1)
		p.add(30)
		p.add(5)
		self.assertTrue(p.peek(), 1)
		p.remove()
		self.assertTrue(p.peek(), 5)
		p.remove()
		self.assertTrue(p.peek(), 10)

	def test_for_add_and_get_size(self):
		p = PriorityQueue()
		p.add(999)
		p.add(222)
		p.add(33)
		p.add(33)
		self.assertTrue(p.size(), 5)
		
	def sift_down_test(self):
		p = PriorityQueue()
		p.add(999)
		p.add(222)
		p.add(33)
		p.add(33)
		self.assertTrue(p.sift_down, 3)
		p.add(45)
		self.assertTrue(p.sift_down, 2)
		p.add(22)

if __name__ == '__main__':
	unittest.main()