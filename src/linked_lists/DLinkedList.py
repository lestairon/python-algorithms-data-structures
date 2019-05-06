import gc

class Node:
  def __init__(self, data_val= None):
    self.data_val = data_val
    self.next_val = None
    self.prev_val = None

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def print_list(self):
    printval = self.head_node
    val = []
    while printval is not None:
      val.append(printval.data_val)
      print(printval.data_val)
      printval = printval.next_val

  # Add to the start
  def insert(self, new_data):
    new_node = Node(new_data)
    new_node.next_val = self.head_node
    if self.head_node is None:
      self.tail_node = new_node
    else:
      self.head_node.prev_val = new_node
    self.head_node = new_node

  # Add to the end
  def append(self, new_data):
    new_node = Node(new_data)
    if self.head_node is None:
      self.head_node = new_node
    else:
      new_node.prev_val = self.tail_node
      self.tail_node.next_val = new_node
    self.tail_node = new_node

  # Deletes the first element in the List
  def shift(self):
    remove_val = self.head_node.next_val
    if remove_val:
      self.head_node = remove_val
      self.head_node.prev_val = None
    else:
      self.head_node = None
      self.tail_node = None

  # Deletes the last element in the List
  def pop(self):
    head = self.head_node
    if head.next_val is None:
      self.tail_node = None
      self.head_node = None
    else:
      self.tail_node.prev_val.next_val = None
      self.tail_node = self.tail_node.prev_val