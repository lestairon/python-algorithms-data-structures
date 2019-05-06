import gc

class Node:

  def __init__ (self, data_val=None):
    self.data_val = data_val
    self.next_val = None

class SingleLinkedList:
  
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  # Print linked list
  def print_list(self):
    printval = self.head_node
    while printval is not None:
      print(printval.data_val)
      printval = printval.next_val

  # Add to the start
  def insert(self, new_data):
    new_node = Node(new_data)
    new_node.next_val = self.head_node
    if self.head_node is None:
      self.tail_node = new_node
    self.head_node = new_node

  # Add to the end
  def append(self, new_data):
    new_node = Node(new_data)
    if self.head_node is None:
      self.head_node = new_node
      self.tail_node = new_node
      return
    tail = self.head_node
    while tail.next_val:
      tail = tail.next_val
    tail.next_val = new_node
    self.tail_node = new_node

  def shift(self):
    remove_val = self.head_node.next_val
    if remove_val:
      self.head_node = remove_val
    else:
      self.head_node = None
      self.tail_node = None

  def pop(self):
    temp = self.head_node
    if temp.next_val:
      while temp.next_val is not None:
        prev = temp
        temp = temp.next_val
      prev.next_val = None
      self.tail_node = prev
    else:
      self.head_node = None
      self.tail_node = None
