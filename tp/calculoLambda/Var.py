from .Asserts import *
from .Types import *

class Var(object):
  def __init__(self, value):
    self.value = value
    self.type = Types.VAR
    self.vtype = None

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.getValue() == other.getValue()
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def getValue(self):
    return self.value

  def getVar(self):
    return self

  def getType(self):
    return self.vtype

  def setType(self, vtype):
    self.vtype = vtype

  def evaluate(self, context):
    if (self.getValue() in context):
      self.setType(context[self.getValue()])
    return self

  def printString(self):
    return self.getValue()

  def printType(self):
    assertTypeNonVar(self)
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return (not self.getValue() in context, self)

  def findAndReplace(self, var, parameter):
    return parameter if self == var else self
