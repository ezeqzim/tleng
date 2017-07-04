from .Type import *
from .Asserts import *

class Zero(object):
  def __init__(self):
    self.value = 0
    self.type = Arrow(Nat())

  def evaluate(self):
    return self

  def printString(self):
    return '0'

  def findAndReplace(self, var, parameter):
    return self

  def printType(self):
    return self.type.printType()

class FTrue(object):
  def __init__(self):
    self.value = True
    self.type = Arrow(Bool())

  def evaluate(self):
    return self

  def printString(self):
    return 'true'

  def findAndReplace(self, var, parameter):
    return self

  def printType(self):
    return self.type.printType()

class FFalse(object):
  def __init__(self):
    self.value = False
    self.type = Arrow(Bool())

  def evaluate(self):
    return self

  def printString(self):
    return 'false'

  def findAndReplace(self, var, parameter):
    return self

  def printType(self):
    return self.type.printType()

class Succ(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def evaluate(self):
    resExpression = self.expression.evaluate()
    assertTypeNat(resExpression)
    resExpression.value += 1
    return resExpression

  def printString(self):
    return 'succ(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    return Succ(self.expression.findAndReplace(var, parameter))

  def printType(self):
    return self.type.printType()

class Pred(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def evaluate(self):
    resExpression = self.expression.evaluate()
    assertTypeNat(resExpression)
    resExpression.value -= 0 if resExpression.value == 0 else 1
    return resExpression

  def printString(self):
    return 'pred(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    return Pred(self.expression.findAndReplace(var, parameter))

  def printType(self):
    return self.type.printType()

class Iszero(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def evaluate(self):
    resExpression = self.expression.evaluate()
    assertTypeNat(resExpression)
    resExpression.value = resExpression.value == 0
    resExpression.type = Bool()
    return resExpression

  def printString(self):
    return 'iszero(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    return Iszero(self.expression.findAndReplace(var, parameter))

  def printType(self):
    return self.type.printType()

class Enclosed(object):
  def __init__(self, expression):
    self.expression = expression
    self.type = expression.type

  def evaluate(self):
    return self.expression.evaluate()

  def printString(self):
    return '(' + self.expression.printString() + ')'

  def findAndReplace(self, var, parameter):
    return Enclosed(self.expression.findAndReplace(var, parameter))

  def printType(self):
    return self.type.printType()
