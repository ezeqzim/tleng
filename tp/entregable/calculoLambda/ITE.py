from .Asserts import *
from .Var import *

class IfThenElse(object):
  def __init__(self, condition, ifTrue, ifFalse):
    self.condition = condition
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.type = ifTrue.getType()

  def getType(self):
    return self.type

  def setType(self, atype):
    self.type = atype

  def getCondition(self):
    return self.condition

  def setCondition(self, condition):
    self.condition = condition

  def getIfTrue(self):
    return self.ifTrue

  def setIfTrue(self, ifTrue):
    self.ifTrue = ifTrue

  def getIfFalse(self):
    return self.ifFalse

  def setIfFalse(self, ifFalse):
    self.ifFalse = ifFalse

  def evaluate(self, context):
    assertNotHasFreeVariables(self.getCondition(), context)
    self.setCondition(self.getCondition().evaluate(context))
    assertTypeBool(self.getCondition())
    assertNotHasFreeVariables(self.getIfTrue(), context)
    assertNotHasFreeVariables(self.getIfFalse(), context)
    self.setIfTrue(self.getIfTrue().evaluate(context))
    self.setIfFalse(self.getIfFalse().evaluate(context))
    assertSameType(self.getIfTrue(), self.getIfFalse())
    self.setType(self.getIfTrue().getType())
    if (self.getCondition().hasFreeVariables({})[0]):
      return self
    if (self.getCondition().getValue()):
      return self.getIfTrue()
    return self.getIfFalse()

  def printString(self):
    return 'if ' + self.getCondition().printString() + ' then ' + self.getIfTrue().printString() + ' else ' + self.getIfFalse().printString()

  def printType(self):
    return self.getType().printType()

  def findAndReplace(self, var, parameter):
    self.setCondition(self.getCondition().findAndReplace(var, parameter))
    self.setIfTrue(self.getIfTrue().findAndReplace(var, parameter))
    self.setIfFalse(self.getIfFalse().findAndReplace(var, parameter))
    return self

  def hasFreeVariables(self, context):
    hasFreeVariables = self.getCondition().hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.getIfTrue().hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.getIfFalse().hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    return (False, hasFreeVariables[1])
