from .Type import *
from .Types import *

class ExpressionMustBeBool(Exception):
  pass

class ExpressionMustBeNat(Exception):
  pass

class ExpressionMustBeLambda(Exception):
  pass

class ExpressionsMustHaveEqualType(Exception):
  pass

class ExpressionMustBeApplicable(Exception):
  pass

def assertTypeBool(expression):
  if (not (expression.getType() == Arrow(Bool()))):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.getType() == Arrow(Nat()))):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertTypeLambda(expression):
  if (not (expression.getType().right is not None)):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Lambda'
    raise ExpressionMustBeLambda(message)

def assertSameType(expression1, expression2):
  if (not (expression1.getType() == expression2.getType())):
    message = 'Las expresiones ' + expression1.printString() + ' y ' + expression2.printString() + ' deben ser del mismo tipo'
    raise ExpressionsMustHaveEqualType(message)

def assertTypeForApplication(expression1, expression2):
  if (not (expression1.getType() == expression2.getType())):
    message = 'La expresion ' + expression2.printString() + ' : ' + expression2.printType() + ' no tiene el tipo correcto para sustituir a ' + expression1.printString() + ' : ' + expression1.printType()
    raise ExpressionMustBeApplicable(message)
