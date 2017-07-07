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

  def getExpression(self):
    return self.expression

  def setExpression(self, expression):
    self.expression = expression

  def evaluate(self, context):
    assertNotHasFreeVariables(self.getExpression(), context)
    self.setExpression(self.getExpression().evaluate(context))
    assertTypeNat(self.getExpression())
    if (not self.getExpression().hasFreeVariables({})[0]):
      self.setValue(self.getValue() + 1)
    return self

  def printString(self):
    return 'succ(' + self.getExpression().printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.getExpression().hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.setExpression(self.getExpression().findAndReplace(var, parameter))
    return self

class Pred(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Nat())

  def getExpression(self):
    return self.expression

  def setExpression(self, expression):
    self.expression = expression

  def evaluate(self, context):
    assertNotHasFreeVariables(self.getExpression(), context)
    self.setExpression(self.getExpression().evaluate(context))
    assertTypeNat(self.getExpression())
    if (not self.getExpression().hasFreeVariables({})[0]):
      oldValue = self.getExpression().getValue()
      if (oldValue == 0):
        return Zero()
      self.getExpression().setValue(oldValue - 1)
      return Zero() if self.getExpression().getValue() == 0 else Succ(self.getExpression())
    return self

  def printString(self):
    return 'pred(' + self.getExpression().printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.getExpression().hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.setExpression(self.getExpression().findAndReplace(var, parameter))
    return self

class Iszero(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return Arrow(Bool())

  def getExpression(self):
    return self.expression

  def setExpression(self, expression):
    self.expression = expression

  def evaluate(self, context):
    assertNotHasFreeVariables(self.getExpression(), context)
    self.setExpression(self.getExpression().evaluate(context))
    assertTypeNat(self.getExpression())
    if (not self.getExpression().hasFreeVariables({})[0]):
      return FTrue() if self.getExpression().getValue() == 0 else FFalse()
    return Iszero(self.getExpression())

  def printString(self):
    return 'iszero(' + self.getExpression().printString() + ')'

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.getExpression().hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    self.setExpression(self.getExpression().findAndReplace(var, parameter))
    return self

class Enclosed(object):
  def __init__(self, expression):
    self.expression = expression

  def getType(self):
    return self.expression.getType()

  def getVar(self):
    return self.expression.getVar()

  def getExpression(self):
    return self.expression

  def setExpression(self, expression):
    self.expression = expression

  def evaluate(self, context):
    return Enclosed(self.getExpression().evaluate(context))

  def printString(self):
    return '(' + self.getExpression().printString() + ')'

  def findAndReplace(self, var, parameter):
    self.setExpression(self.getExpression().findAndReplace(var, parameter))
    return self

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    return self.getExpression().hasFreeVariables(context)

  def evalWith(self, parameter, context):
    return self.getExpression().evalWith(parameter, context)

