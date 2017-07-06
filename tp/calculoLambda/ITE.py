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

  def evaluate(self, context):
    assertNotHasFreeVariables(self.condition, context)
    self.condition = self.condition.evaluate(context)
    assertTypeBool(self.condition)
    assertNotHasFreeVariables(self.ifTrue, context)
    assertNotHasFreeVariables(self.ifFalse, context)
    self.ifTrue = self.ifTrue.evaluate(context)
    self.ifFalse = self.ifFalse.evaluate(context)
    assertSameType(self.ifTrue, self.ifFalse)
    self.type = self.ifTrue.getType()
    if (self.condition.hasFreeVariables({})[0]):
      return self
    if (self.condition.getValue()):
      return self.ifTrue
    return self.ifFalse

  def printString(self):
    return 'if ' + self.condition.printString() + ' then ' + self.ifTrue.printString() + ' else ' + self.ifFalse.printString()

  def printType(self):
    return self.getType().printType()

  def findAndReplace(self, var, parameter):
    self.condition = self.condition.findAndReplace(var, parameter)
    self.ifTrue = self.ifTrue.findAndReplace(var, parameter)
    self.ifFalse = self.ifFalse.findAndReplace(var, parameter)
    return self

  def hasFreeVariables(self, context):
    hasFreeVariables = self.condition.hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.ifTrue.hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.ifFalse.hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    return (False, hasFreeVariables[1])
