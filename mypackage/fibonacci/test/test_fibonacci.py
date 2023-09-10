"""Tests for fibonacci module."""
from mypackage.fibonacci.fibonacci import calculate_fibonacci


def test_calculate_fibonacci():
  """Test fibonacci calculator."""
  result = calculate_fibonacci(10)
  assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
