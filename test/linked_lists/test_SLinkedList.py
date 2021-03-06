from src.linked_lists.SLinkedList import SingleLinkedList
import unittest

class TestLinkedList(unittest.TestCase):

  def setUp(self):
    self.test_list = SingleLinkedList()
    self.data1 = 5
    self.data2 = 4

  def test_insert_data(self):
    self.test_list.insert(self.data1)
    # Check if assigning it to head node
    self.assertEqual(self.data1, self.test_list.head_node.data_val)
    self.assertEqual(self.data1, self.test_list.tail_node.data_val)
    # Check if head is reassigned and tail was the previous head
    self.test_list.insert(self.data2)
    self.assertEqual(self.data2, self.test_list.head_node.data_val)
    self.assertEqual(self.data1, self.test_list.tail_node.data_val)

  def test_append_data(self):
    self.test_list.append(self.data1)
    self.assertEqual(self.data1, self.test_list.head_node.data_val)      
    self.assertEqual(self.data1, self.test_list.tail_node.data_val)
    self.test_list.append(self.data2)
    self.assertEqual(self.data2, self.test_list.tail_node.data_val)
    self.assertEqual(self.data1, self.test_list.head_node.data_val)
  
  def test_shift_data(self):
    self.test_list.insert(self.data1)
    # Check if shifts the only object
    self.test_list.shift()
    self.assertIsNone(self.test_list.head_node)
    # Check if shifts when multiple objects
    self.test_list.insert(self.data1)
    self.test_list.insert(self.data2)
    self.test_list.shift()
    self.assertEqual(self.data1, self.test_list.head_node.data_val)
    self.assertEqual(self.data1, self.test_list.tail_node.data_val)

  def test_pop_data(self):
    self.test_list.insert(self.data1)
    self.test_list.append(self.data2)
    self.assertIsNot(self.data1, self.test_list.tail_node.data_val)
    self.test_list.pop()
    self.assertEqual(self.data1, self.test_list.tail_node.data_val)

  def test_pop_deletes_head_and_tail(self):
    self.test_list.insert(self.data1)
    self.test_list.pop()
    self.assertIsNone(self.test_list.head_node)
    self.assertIsNone(self.test_list.tail_node)

  def test_shift_deletes_head_and_tail(self):
    self.test_list.insert(self.data1)
    self.test_list.shift()
    self.assertIsNone(self.test_list.tail_node)
    self.assertIsNone(self.test_list.head_node)

    
if __name__ == '__main__':
  unittest.main()