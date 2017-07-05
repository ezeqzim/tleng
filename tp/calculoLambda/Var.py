from .Types import *

class FreeVariable(Exception):
  pass

def assertTypeNonVar(expression):
  if (expression.vtype is None):
    message = 'La variable ' + expression.value + ' esta libre'
    raise FreeVariable(message)

class Var(object):
  def __init__(self, value):
    self.value = value
    self.type = Types.VAR
    self.vtype = None

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.value == other.value
    return False

  def __ne__(self, other):
    return not self.__eq__(self, other)

  def getValue(self):
    return self.value

  def getType(self):
    return self.vtype

  def setType(self, vtype):
    self.vtype = vtype

  def evaluate(self, context):
    if (self.value in context):
      self.vtype = context[self.value]
    return self

  def printString(self):
    return self.value

  def printType(self):
    assertTypeNonVar(self)
    return self.getType().printType()

  def hasFreeVariables(self, context):
    if (self.value in context):
      self.vtype = context[self.value]
    return not self.value in context

  def findAndReplace(self, var, parameter):
    return parameter if self == var else self
