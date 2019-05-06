class Node:
  def __init__ (self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLikedList:
  def __init__(self):
    self.headval = None

  # Print linked list
  def PrintList(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval

  # Add to the start
  def AddFirst(self, newdata):
    NewNode = Node(newdata)
    NewNode.nextval = self.headval
    self.headval = NewNode
