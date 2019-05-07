from src.stack.StackList import Stack
import unittest

class TestLinkedList(unittest.TestCase):

  def setUp(self):
    self.test_stack = Stack()
    self.data1 = 5
    self.data2 = 6

  def test_push_new_data(self):
    self.test_stack.push(self.data1)
    self.assertEqual(1, self.test_stack.count())

  def test_pop_existing_data(self):
    self.test_stack.push(self.data1)
    self.test_stack.pop()
    self.assertEqual(0, self.test_stack.count())

  def test_count_data(self):
    x = 10
    self.assertEqual(0, self.test_stack.count())
    for _ in range(x):
      self.test_stack.push(self.data1)
    self.assertEqual(x, self.test_stack.count())

  def test_clear_data(self):
    x = 10
    for _ in range(x):
      self.test_stack.push(self.data1)
    self.assertEqual(x, self.test_stack.count())
    self.test_stack.clear()
    self.assertEqual(0, self.test_stack.count())

  def test_peek_data(self):
    with self.assertRaises(IndexError) as ex:
      self.test_stack.peek()
    self.assertTrue(ex.exception)
    self.test_stack.push(self.data1)
    self.assertEqual(self.data1, self.test_stack.peek())

if __name__ == '__main__':
  unittest.main()