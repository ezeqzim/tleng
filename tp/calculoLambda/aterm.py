from .types import *

class ATerm(object):
  def printString(self):
    return str(self.value)

class ATrue(ATerm):
  def __init__(self):
    self.value = True
    self.type = Types.BOOL

class AFalse(ATerm):
  def __init__(self):
    self.value = False
    self.type = Types.BOOL

class AZero(ATerm):
  def __init__(self):
    self.value = 0
    self.type = Types.NAT

class AVar(ATerm):
  def __init__(self, value):
    self.value = value
    self.type = Types.VAR

class Abstraction(ATerm):
  def __init__(self, var, ftype, body):
    self.var = var
    self.ftype = ftype
    self.expression = lambda x: body(x)
    self.value = body.value
    self.type = Types.LAMBDA

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.ftype.printString() + '.' + self.expression.printString()

class Application(ATerm):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  # def printString(self):
  #   if (self.type == Types.LAMBDA):
  #     return self.expression.printString()

class Succ(ATerm):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value + 1
    self.type = Types.NAT

class Pred(ATerm):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = 0 if expression.value == 0 else expression.value - 1
    self.type = Types.NAT

class Iszero(ATerm):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value == 0
    self.type = Types.BOOL

class IfThenElse(ATerm):
  def __init__(self, condition, ifTrue, ifFalse):
    assertTypeBool(condition)
    assertSameType(ifTrue, ifFalse)
    self.expression = lambda x, y, z: y if x else z
    self.condition = condition
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.value = ifTrue.value if condition.value else ifFalse.value
    self.type = ifTrue.type
