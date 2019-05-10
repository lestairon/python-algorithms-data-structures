import gc


class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None
        self.prev_value = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def print_list(self):
        printvalue = self.head_node
        value = []
        while printvalue is not None:
            value.append(printvalue.data_value)
            print(printvalue.data_value)
            printvalue = printvalue.next_value

    # Add to the start
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next_value = self.head_node
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.head_node.prev_value = new_node
        self.head_node = new_node

    # Add to the end
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.prev_value = self.tail_node
            self.tail_node.next_value = new_node
        self.tail_node = new_node

    def add_before(self, search_value, new_data):
        new_node = Node(new_data)
        current = self.head_node
        while current is not None:
            if current.data_value == search_value:
                if current.prev_value is None:
                    new_node.next_value = current
                    self.head_node = new_node
                    current.prev_value = new_node
                    self.tail_node = current
                else:
                    if current == self.tail_node:
                        self.tail_node = current
                    new_node.prev_value = current.prev_value
                    new_node.next_value = current
                    current.prev_value.next_value = new_node
                    current.prev_value = new_node
            current = current.next_value
        if current is None:
            return

    # Deletes the first element in the List
    def shift(self):
        remove_value = self.head_node.next_value
        if remove_value:
            self.head_node = remove_value
            self.head_node.prev_value = None
        else:
            self.head_node = None
            self.tail_node = None

    # Deletes the last element in the List
    def pop(self):
        head = self.head_node
        if head.next_value is None:
            self.tail_node = None
            self.head_node = None
        else:
            self.tail_node.prev_value.next_value = None
            self.tail_node = self.tail_node.prev_value
