from .Asserts import *

class Types:
  VAR = 'VAR'

class Var(object):
  def __init__(self, value):
    self.value = value
    self.type = Types.VAR

  def evaluate(self):
    return self

  def printString(self):
    return str(self.value)

  def findAndReplace(self, var, parameter):
    return parameter if self.value == var else self

  def printType(self):
    message = 'La variable ' + self.value + ' esta libre'
    raise FreeVariable(message)
    # return self.type.printType()
