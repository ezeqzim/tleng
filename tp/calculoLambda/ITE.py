from .Asserts import *

class IfThenElse(object):
  def __init__(self, condition, ifTrue, ifFalse):
    self.condition = condition
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.type = ifTrue.type

  def evaluate(self):
    resCond = self.condition.evaluate()
    assertTypeBool(resCond)
    resTrue = self.ifTrue.evaluate()
    resFalse = self.ifFalse.evaluate()
    assertSameType(resTrue, resFalse)
    if (resCond.value):
      return resTrue
    return resFalse

  def printString(self):
    return 'if ' + self.condition.printString() + ' then ' + self.ifTrue.printString() + ' else ' + self.ifFalse.printString()

  def findAndReplace(self, var, parameter):
    return IfThenElse(self.condition.findAndReplace(var, parameter), self.ifTrue.findAndReplace(var, parameter), self.ifFalse.findAndReplace(var, parameter))
