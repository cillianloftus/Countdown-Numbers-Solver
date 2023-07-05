from calculation import Calculation
from solutions import Solutions
import re
import sys

assert sys.version_info >= (3, 6)

def main():
  try:
    target = int(sys.argv[1])
    numbers_raw = (int(sys.argv[n + 2]) for n in range(6))
    numbers = tuple(sorted(numbers_raw, reverse=True))
  except (IndexError, ValueError):
    print('You must provide both a target and numbers.')
    return
  finally:
    solve(target, numbers)

def output(target, difference, results):
  print(f'\nThe closest results differ from {target} by {difference}.\n')
  for result in results:
    print(f'{result.answer} = {result.expression}')
  print()

def parse_expression(expression):
  match = re.search(r"\(([^()]+)\)", expression)
  print(match)

def solve(target, numbers):
  best_results = []
  smallest_difference = target
  solutions = Solutions(numbers)

  for calculation in solutions.walk():
    difference = abs(calculation.answer - target)
    if difference < smallest_difference:
      best_results = [calculation]
      smallest_difference = difference
    elif difference == smallest_difference:
      best_results.append(calculation)

  output(target, smallest_difference, best_results)

if __name__ == '__main__':
  main()
