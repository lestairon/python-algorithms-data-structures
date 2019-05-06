import gc

class Node:
  def __init__ (self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __init__(self):
    self.headval = None

  # Print linked list
  def print_list(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval

  # Add to the start
  def add_first(self, newdata):
    NewNode = Node(newdata)
    NewNode.nextval = self.headval
    self.headval = NewNode

  # Add to the end
  def add_last(self, newdata):
    NewNode = Node(newdata)
    if self.headval is None:
      self.headval = NewNode
      return
    tail = self.headval
    while tail.nextval:
      tail = tail.nextval
    tail.nextval = NewNode

  def remove_first(self):
    removeval = self.headval.nextval
    if removeval:
      self.headval = removeval
    else:
      self.headval = None

  def remove_last(self):
    temp = self.headval
    if temp.nextval:
      while temp.nextval is not None:
        prev = temp
        temp = temp.nextval
      prev.nextval = None
    else:
      self.headval = None
