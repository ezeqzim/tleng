class Lambda(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return self.expression.printString()
