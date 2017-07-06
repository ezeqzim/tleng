from .Asserts import *
from .Type import *
from .Var import *

class Zero(object):
  def __init__(self):
    self.value = 0

  def getValue(self):
    return self.value

  def getType(self):
    return Arrow(Nat())

  def evaluate(self, context):
    return self

  def printString(self):
    return '0'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return (False, self)

  def findAndReplace(self, var, parameter):
    return self

class FTrue(object):
  def __init__(self):
    self.value = True

  def getValue(self):
    return self.value

  def getType(self):
    return Arrow(Bool())

  def evaluate(self, context):
    return self

  def printString(self):
    return 'true'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return (False, self)

  def findAndReplace(self, var, parameter):
    return self

class FFalse(object):
  def __init__(self):
    self.value = False

  def getValue(self):
    return self.value

  def getType(self):
    return Arrow(Bool())

  def evaluate(self, context):
    return self

  def printString(self):
    return 'false'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return (False, self)

  def findAndReplace(self, var, parameter):
    return self

class Succ(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = 0

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def getType(self):
    return Arrow(Nat())

  def evaluate(self, context):
    assertNotHasFreeVariables(self.expression, context)
    self.expression = self.expression.evaluate(context)
    assertTypeNat(self.expression)
    if (not self.expression.hasFreeVariables({})[0]):
      self.setValue(self.getValue() + 1)
    return self

  def printString(self):
    return 'succ(' + self.expression.printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.expression = self.expression.findAndReplace(var, parameter)
    return self

class Pred(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Nat())

  def evaluate(self, context):
    assertNotHasFreeVariables(self.expression, context)
    self.expression = self.expression.evaluate(context)
    assertTypeNat(self.expression)
    if (not self.expression.hasFreeVariables({})[0]):
      oldValue = self.expression.getValue()
      if (oldValue == 0):
        return Zero()
      self.expression.setValue(oldValue - 1)
      return Zero() if self.expression.getValue() == 0 else Succ(self.expression)
    return self

  def printString(self):
    return 'pred(' + self.expression.printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.expression = self.expression.findAndReplace(var, parameter)
    return self

class Iszero(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Bool())

  def evaluate(self, context):
    assertNotHasFreeVariables(self.expression, context)
    resExpression = self.expression.evaluate(context)
    assertTypeNat(resExpression)
    if (not self.expression.hasFreeVariables({})[0]):
      return FTrue() if resExpression.getValue() == 0 else FFalse()
    return Iszero(resExpression)

  def printString(self):
    return 'iszero(' + self.expression.printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.expression = self.expression.findAndReplace(var, parameter)
    return self

class Enclosed(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return self.expression.getType()

  def getVar(self):
    return self.expression.getVar()

  def evaluate(self, context):
    return Enclosed(self.expression.evaluate(context))

  def printString(self):
    return '(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    self.expression = self.expression.findAndReplace(var, parameter)
    return self

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def evalWith(self, parameter, context):
    return self.expression.evalWith(parameter, context)

