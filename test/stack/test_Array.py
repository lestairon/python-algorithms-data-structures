from src.stack.Array import Stack
import unittest

class TestLinkedList(unittest.TestCase):

  def setUp(self):
    self.test_stack = Stack()
    self.data1 = 5
    self.data2 = 6

  def test_push_data(self):
    self.test_stack.push(self.data1)
    self.assertEqual(self.data1, self.test_stack.peek())
    self.test_stack.push(self.data2)
    self.assertEqual(self.data2, self.test_stack.peek())

  def test_pop_data(self):
    self.test_stack.push(self.data1)
    self.test_stack.push(self.data2)
    self.assertEqual(self.data2, self.test_stack.peek())
    self.test_stack.pop()
    self.assertEqual(self.data1, self.test_stack.peek())

  def test_count_data(self):
    self.assertEqual(0, self.test_stack.count())
    x = 12
    for _ in range(x):
      self.test_stack.push("data")
    self.assertEqual(x, self.test_stack.count())

  def test_clear_data(self):
    x = 12
    for _ in range(x):
      self.test_stack.push("data")
    self.assertEqual(x, self.test_stack.count())
    self.test_stack.clear()
    self.assertEqual(0, self.test_stack.count())

if __name__ == '__main__':
  unittest.main()