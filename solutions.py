from itertools import combinations
from group import Group

class Solutions:
  def __init__(self, numbers):
    self.numbers = numbers
    self.size = len(numbers)
    self.all_groups = self.unique_groups()

  def unique_groups(self):
    all_groups = {}
    all_numbers = self.numbers
    size = self.size
    for m in range(1, size+1):
      for numbers in combinations(all_numbers, m):
        if numbers in all_groups:
            continue
        all_groups[numbers] = Group(numbers, all_groups)
    return all_groups

  def walk(self):
    for group in self.all_groups.values():
      yield from group.calculations
