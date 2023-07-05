from calculation import Calculation
from itertools import combinations, product, zip_longest
from functools import lru_cache

class Group:
  def __init__(self, numbers, all_groups):
    self.numbers = numbers
    self.size = len(numbers)
    self.partitions = list(self.partition_into_unique_pairs(all_groups))
    self.calculations = list(self.perform_calculations())

  def __repr__(self):
    return str(self.numbers)

  def partition_into_unique_pairs(self, all_groups):
    if self.size == 1: return

    numbers, size = self.numbers, self.size
    limits = (self.half_binom(size, size // 2), )
    unique_numbers = set()
    for m, limit in zip_longest(range((size + 1) // 2, size), limits):
      for num1, num2 in self.paired_combinations(numbers, m, limit):
        if num1 in unique_numbers: continue
        unique_numbers.add(num1)
        group1, group2 = all_groups[num1], all_groups[num2]
        yield (group1, group2)

  def perform_calculations(self):
    if self.size == 1:
      yield Calculation.singleton(self.numbers[0])
      return
    for group1, group2 in self.partitions:
      for calc1, calc2 in product(group1.calculations, group2.calculations):
        yield from Calculation.generate(calc1, calc2)

  @classmethod
  def paired_combinations(cls, numbers, m, limit):
    for cnt, numbers1 in enumerate(combinations(numbers, m), 1):
      numbers2 = tuple(cls.filtering(numbers, numbers1))
      yield (numbers1, numbers2)
      if cnt == limit:
          return

  # Filter elements out of an iterable, return the remaining elements
  @staticmethod
  def filtering(iterable, elements):
    elems = iter(elements)
    k = next(elems, None)
    for n in iterable:
      if n == k:
        k = next(elems, None)
      else:
        yield n

  @staticmethod
  @lru_cache()
  def half_binom(n, k):
    if n % 2 == 1:
      return None
    prod = 1
    for m, l in zip(reversed(range(n+1-k, n+1)), range(1, k+1)):
      prod = (prod*m)//l
    return prod // 2
