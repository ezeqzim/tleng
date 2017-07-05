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
    if (self.condition.hasFreeVariables(context)):
      self.condition.printType() # raise FreeVariable
    resCond = self.condition.evaluate(context)
    assertTypeBool(resCond)
    if (self.ifTrue.hasFreeVariables(context)):
      self.ifTrue.printType() # raise FreeVariable
    if (self.ifFalse.hasFreeVariables(context)):
      self.ifFalse.printType() # raise FreeVariable
    resTrue = self.ifTrue.evaluate(context)
    resFalse = self.ifFalse.evaluate(context)
    assertSameType(resTrue, resFalse)
    if (self.condition.hasFreeVariables({})):
      return self
    if (resCond.value):
      return resTrue
    return resFalse

  def printString(self):
    return 'if ' + self.condition.printString() + ' then ' + self.ifTrue.printString() + ' else ' + self.ifFalse.printString()

  def printType(self):
    return self.getType()

  def findAndReplace(self, var, parameter):
    return IfThenElse(self.condition.findAndReplace(var, parameter), self.ifTrue.findAndReplace(var, parameter), self.ifFalse.findAndReplace(var, parameter))

  def hasFreeVariables(self, context):
    return self.condition.hasFreeVariables(context) or self.ifTrue.hasFreeVariables(context) or self.ifFalse.hasFreeVariables(context)
