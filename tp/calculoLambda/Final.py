from .Types import *
from .Asserts import *

class Final(object):
  def printString(self):
    return str(self.value)

class Zero(Final):
  def __init__(self):
    self.value = 0
    self.type = Types.NAT

class FTrue(Final):
  def __init__(self):
    self.value = True
    self.type = Types.BOOL

class FFalse(Final):
  def __init__(self):
    self.value = False
    self.type = Types.BOOL

class IfThenElse(Final):
  def __init__(self, condition, ifTrue, ifFalse):
    # assertTypeBool(condition)
    # assertSameType(ifTrue, ifFalse)
    self.expression = lambda x, y, z: y if x else z
    self.condition = condition
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.value = ifTrue.value if condition.value else ifFalse.value
    self.type = ifTrue.type

class Succ(Final):
  def __init__(self, expression):
    # assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value + 1
    self.type = Types.NAT

class Pred(Final):
  def __init__(self, expression):
    # assertTypeNat(expression)
    self.expression = expression
    self.value = 0 if expression.value == 0 else expression.value - 1
    self.type = Types.NAT

class Iszero(Final):
  def __init__(self, expression):
    # assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value == 0
    self.type = Types.BOOL

class Enclosed(Final):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return '(' + self.expression.printString() + ')'

class Abstraction(Final):
  def __init__(self, var, ftype, body):
    self.var = var
    self.ftype = ftype
    self.expression = lambda x: body(x)
    self.value = body.value
    self.type = Types.LAMBDA

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.ftype.printString() + '.' + self.expression.printString()
