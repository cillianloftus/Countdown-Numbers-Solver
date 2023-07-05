class Calculation:
  def __init__(self, expression, answer, is_singleton=False):
    self.answer = answer
    self.expression = expression
    self.is_singleton = is_singleton

  def __repr__(self):
    return self.expression

  # Generate new calculations from two given calculations by performing arithmetic operations on each
  @classmethod
  def generate(class_self, a, b):
    if a.answer < b.answer:
      a, b = b, a
    
    for result, operation in class_self.operations(a.answer, b.answer):
      expression_a = f'{a.expression}' if a.is_singleton else f'({a.expression})'
      expression_b = f'{b.expression}' if b.is_singleton else f'({b.expression})'
      yield class_self(f'{expression_a} {operation} {expression_b}', result)

  # Generates a singleton calculation
  @classmethod
  def singleton(class_self, n):
    return class_self(f'{n}', n, is_singleton=True)

  @staticmethod
  def operations(x, y):
    yield (x + y, '+')
    # Exclude non-positive results
    if x > y:
      yield (x - y, '-')
    # Exclude trivial results
    if y > 1 and x > 1:
      yield (x * y, 'x')
    # Exlcude trivial and non-integer results
    if y > 1 and x % y == 0:
      yield (x // y, '/')
