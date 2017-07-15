class Start(object):
  def __init__(self, expression):
    self.expression = expression

  def evaluate(self):
    return Start(self.expression.evaluate({}))

  def printString(self):
    return self.expression.printString() + ' : ' + self.expression.printType()
