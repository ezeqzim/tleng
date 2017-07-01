class ExpressionMustBeBool(Exception):
  pass

class ExpressionMustBeNat(Exception):
  pass

class ExpressionsMustHaveEqualType(Exception):
  pass

class ExpressionMustBeApplicable(Exception):
  pass

def assertTypeBool(expression):
  if (not (expression.type[0] == Types.BOOL)):
    message = 'La expresion ' + str(expression.value) + ' debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.type[0] == Types.NAT)):
    message = 'La expresion ' + str(expression.value) + ' debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertSameType(expression1, expression2):
  if (not (expression1.type == expression2.type)):
    message = 'Las expresiones ' + str(expression1.value) + ' y ' + str(expression2.value) + ' deben ser del mismo tipo'
    raise ExpressionsMustHaveEqualType(message)

def assertTypeForApplication(expression1, expression2):
  message = 'La expresion ' + str(expression2.value) + ':' + str(expression2.type) + ' no tiene el tipo correcto para aplicarse a ' + str(expression1.value) + ':' + str(expression1.type)
  if (len(expression1.type) <= len(expression2.type)):
      raise ExpressionMustBeApplicable(message)
  for i in range(0, len(expression2.type)):
    if (not (expression1.type[i] == expression2.type[i])):
      raise ExpressionMustBeApplicable(message)

class Types:
  NAT = 'NAT'
  BOOL = 'BOOL'
  VAR = 'VAR'

class Aux(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return self.expression.printString() + ':' + self.expression.type

class ATerm(object):
  def printString(self):
    return str(self.value)

class ATrue(ATerm):
  def __init__(self):
    self.value = True
    self.type = [Types.BOOL]

class AFalse(ATerm):
  def __init__(self):
    self.value = False
    self.type = [Types.BOOL]

class AZero(ATerm):
  def __init__(self):
    self.value = 0
    self.type = [Types.NAT]

class AVar(ATerm):
  def __init__(self, value):
    self.value = value
    self.type = [Types.VAR]

class Type(object):
  def printString(self):
    return str(self.value[0])

class Bool(Type):
  def __init__(self, value):
    self.value = [Types.BOOL]

class Nat(Type):
  def __init__(self, value):
    self.value = [Types.NAT]

class Arrow(Type):
  def __init__(self, left, right = None):
    self.left = left
    self.right = right

  def printString(self):
    if (self.right is None):
      return self.left.printString()
    return self.left.printString() + ' -> ' + self.right.printString()

class Term(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return '(' + self.expression.printString() + ')'

class Application(Term):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return self.expression.printString()

class Succ(Term):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value + 1
    self.type = Types.NAT

  def printString(self):
    return 'succ(' + self.expression.printString() + ')'

class Pred(Term):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = 0 if expression.value == 0 else expression.value - 1
    self.type = Types.NAT

  def printString(self):
    return 'pred(' + self.expression.printString() + ')'

class Iszero(Term):
  def __init__(self, expression):
    assertTypeNat(expression)
    self.expression = expression
    self.value = expression.value == 0
    self.type = Types.BOOL

  def printString(self):
    return 'iszero(' + self.expression.printString() + ')'

class IfThenElse(Term):
  def __init__(self, condition, ifTrue, ifFalse):
    assertTypeBool(condition)
    assertSameType(ifTrue, ifFalse)
    self.condition = condition
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.value = ifTrue.value if condition.value else ifFalse.value
    self.type = ifTrue.type

  def printString(self):
    return 'if ' + self.condition.printString() + ' then ' + self.ifTrue.printString() + ' else ' + self.ifFalse.printString()

class Abstraction(Term):
  def __init__(self, var, ftype, body):
    self.var = var
    self.ftype = ftype
    self.expression = body
    self.value = body.value
    self.type = [ftype] + body.type

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.ftype.printString() + '.' + self.expression.printString()

class App(Term):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return self.expression.printString()

class AppList(App):
  def __init__(self, app, expression):
    assertTypeForApplication(app, expression)
    self.app = app
    self.expression = expression
    self.value = app.value(expression.value)
    self.type = afterApplicationType(app.type, expression.type)

  def printString(self):
    return '(' + self.app.printString() + ') ' + self.expression.printString()
