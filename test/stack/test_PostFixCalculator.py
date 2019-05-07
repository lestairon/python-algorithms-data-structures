from src.stack.PostFixCalculator import PostfixCalculator
import unittest

class TestLinkedList(unittest.TestCase):

  def test_calculator(self):
    calculator = PostfixCalculator()
    result = calculator.calculate(5, 6, 7, '*', '+', 1, '-')
    self.assertEqual(46, result)


if __name__ == '__main__':
  unittest.main()