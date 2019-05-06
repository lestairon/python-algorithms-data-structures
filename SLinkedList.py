import gc

class Node:
  def __init__ (self, data_val=None):
    self.data_val = data_val
    self.next_val = None

class SLinkedList:
  def __init__(self):
    self.head_val = None

  # Print linked list
  def print_list(self):
    printval = self.head_val
    while printval is not None:
      print(printval.data_val)
      printval = printval.next_val

  # Add to the start
  def add_first(self, new_data):
    new_node = Node(new_data)
    new_node.next_val = self.head_val
    self.head_val = new_node

  # Add to the end
  def add_last(self, new_data):
    new_node = Node(new_data)
    if self.head_val is None:
      self.head_val = new_node
      return
    tail = self.head_val
    while tail.next_val:
      tail = tail.next_val
    tail.next_val = new_node

  def remove_first(self):
    remove_val = self.head_val.next_val
    if remove_val:
      self.head_val = remove_val
    else:
      self.head_val = None

  def remove_last(self):
    temp = self.head_val
    if temp.next_val:
      while temp.next_val is not None:
        prev = temp
        temp = temp.next_val
      prev.next_val = None
    else:
      self.head_val = None
