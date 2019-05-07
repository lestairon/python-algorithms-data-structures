import gc


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None
        self.prev_val = None


class QueueList:
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

    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.prev_val = self.tail_node
            self.tail_node.next_val = new_node
        self.tail_node = new_node

    def dequeue(self):
        if self.head_node is None:
            raise IndexError('Queue is already empty')
        else:
            remove_val = self.head_node.next_val
            if remove_val:
                self.head_node = remove_val
                self.head_node.prev_val = None
            else:
                self.head_node = None
                self.tail_node = None

    def peek(self):
        if self.head_node is None:
            raise IndexError('Queue is empty')
        else:
            return self.head_node.data_val

    def count(self):
        temp = self.head_node
        count = 1
        if temp:
            while temp.next_val is not None:
                count += 1
                temp = temp.next_val
            return count
        else:
            return 0

    def clear(self):
        self.head_node = None
        self.tail_node = None

    def enumerate(self):
        printval = self.head_node
        while printval is not None:
            print(printval.data_val)
            printval = printval.next_val
