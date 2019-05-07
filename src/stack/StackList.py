import gc


class Node:

    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next_val = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError('Stack is already Empty')
        else:
            popped = self.head.data_val
            self.head = self.head.next_val
            return popped

    def peek(self):
        if self.head is None:
            raise IndexError('Stack is Empty')
        else:
            return self.head.data_val

    def count(self):
        temp = self.head
        count = 1
        if temp:
            while temp.next_val is not None:
                count += 1
                temp = temp.next_val
            return count
        else:
            return 0

    def clear(self):
        self.head = None

    def enumerate(self):
        printval = self.head
        while printval is not None:
            print(printval.data_val)
            printval = printval.next_val
