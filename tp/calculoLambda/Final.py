from .Asserts import *
from .Type import *
from .Var import *

class Zero(object):
  def __init__(self):
    self.value = 0

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def getType(self):
    return Arrow(Nat())

  def evaluate(self, context):
    return self

  def printString(self):
    return '0'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return False

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
    return False

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
    return False

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
    if (self.expression.hasFreeVariables(context)):
      self.expression.printType() # raise FreeVariable
    resExpression = self.expression.evaluate(context)
    assertTypeNat(resExpression)
    if (not self.expression.hasFreeVariables({})):
      resExpression.setValue(self.getValue() + 1)
      return Succ(resExpression)
    return Succ(resExpression)

  def printString(self):
    return 'succ(' + self.expression.printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    return Succ(self.expression.findAndReplace(var, parameter))

class Pred(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Nat())

  def evaluate(self, context):
    if (self.expression.hasFreeVariables(context)):
      self.expression.printType() # raise FreeVariable
    resExpression = self.expression.evaluate(context)
    assertTypeNat(resExpression)
    if (not self.expression.hasFreeVariables({})):
      oldValue = resExpression.getValue()
      if (oldValue == 0):
        return Zero()
      resExpression.setValue(oldValue - 1)
      return Zero() if resExpression.value == 0 else Succ(resExpression)
    return Pred(resExpression)

  def printString(self):
    return 'pred(' + self.expression.printString() + ')'

  def printType(self):
    return self.type.printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    return Pred(self.expression.findAndReplace(var, parameter))

class Iszero(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Bool())

  def evaluate(self, context):
    if (self.expression.hasFreeVariables(context)):
      self.expression.printType() # raise FreeVariable
    resExpression = self.expression.evaluate(context)
    assertTypeNat(resExpression)
    if (not self.expression.hasFreeVariables({})):
      return FTrue() if resExpression.getValue() == 0 else FFalse()
    return Iszero(resExpression)

  def printString(self):
    return 'iszero(' + self.expression.printString() + ')'

  def printType(self):
    return self.type.printType()

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    return Iszero(self.expression.findAndReplace(var, parameter))

class Enclosed(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return self.expression.getType()

  def evaluate(self, context):
    return Enclosed(self.expression.evaluate(context))

  def printString(self):
    return '(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    return Enclosed(self.expression.findAndReplace(var, parameter))

  def printType(self):
    return '(' + self.getType().printType() + ')'

  def hasFreeVariables(self, context):
    return self.expression.hasFreeVariables(context)

  def evalWith(self, parameter, context):
    return self.expression.evalWith(parameter, context)

