from .types import *

class Start(object):
  def __init__(self, expression):
    self.expression = expression
    self.type = expression.type

  def printString(self):
    return self.expression.printString() + ':' + self.expression.type
