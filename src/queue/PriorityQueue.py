from src.linked_lists.DLinkedList import DoublyLinkedList


class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def print_list(self):
        printval = self.queue.head_node
        val = []
        while printval is not None:
            val.append(printval.data_value)
            print(printval.data_value)
            printval = printval.next_value

    def enqueue(self, new_data):
        if self.queue.head_node is None:
            self.queue.append(new_data)
        else:
            current_node = self.queue.head_node
            while current_node is not None and current_node.data_value > new_data:
                current_node = current_node.next_value
            if current_node is None:
                self.queue.append(new_data)
            else:
                self.queue.add_before(current_node.data_value, new_data)

    def dequeue(self):
        if self.queue.head_node is None:
            raise IndexError('Queue is already empty')
        else:
            remove_val = self.queue.head_node.next_value
            if remove_val:
                self.queue.head_node = remove_val
                self.queue.head_node.prev_value = None
            else:
                self.queue.head_node = None
                self.queue.tail_node = None

    def peek(self):
        if self.queue.head_node is None:
            raise IndexError('Queue is empty')
        else:
            return self.queue.head_node.data_val

    def count(self):
        temp = self.queue.head_node
        count = 1
        if temp:
            while temp.next_value is not None:
                count += 1
                temp = temp.next_value
            return count
        else:
            return 0

    def clear(self):
        self.queue.head_node = None
        self.queue.tail_node = None

    def enumerate(self):
        printval = self.queue.head_node
        while printval is not None:
            print(printval.data_value)
            printval = printval.next_value