"""Fibonacci module docstring."""
from typing import List


def calculate_fibonacci(n: int) -> List[int]:
  """Calculate fibonacci number.

  Args:
    n: Input number.

  Returns:
    A list of fibonacci number for the given input.
  """
  fib_sequence = [0, 1]
  while len(fib_sequence) < n:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)
  return fib_sequence
