from src.queue.QueueArray import QueueArray
import unittest


class TestQueueArray(unittest.TestCase):

    def setUp(self):
        self.test_queue = QueueArray()
        self.data1 = 5
        self.data2 = 4

    def test_enqueue(self):
        self.test_queue.enqueue(self.data1)
        self.assertEqual(self.data1, self.test_queue.peek())

    def test_dequeue(self):
        self.test_queue.enqueue(self.data1)
        self.test_queue.dequeue()
        self.assertEqual(0, self.test_queue.count())
        x = 20
        for _ in range(x):
            self.test_queue.enqueue(self.data1)
        self.test_queue.dequeue()
        self.assertEqual(x-1, self.test_queue.count())

    def test_peek(self):
        self.test_queue.enqueue(self.data1)
        self.assertEqual(self.data1, self.test_queue.peek())
        # should not return the last added value
        self.test_queue.enqueue(self.data2)
        self.assertEqual(self.data1, self.test_queue.peek())

    def test_count(self):
        self.test_queue.enqueue(self.data1)
        self.assertEqual(1, self.test_queue.count())
        x = 20
        for _ in range(x):
            self.test_queue.enqueue(self.data1)
        self.assertEqual(x+1, self.test_queue.count())

    def test_clear(self):
        x = 20
        for _ in range(x):
            self.test_queue.enqueue(self.data1)
        self.assertEqual(x, self.test_queue.count())
        self.test_queue.clear()
        self.assertEqual(0, self.test_queue.count())
