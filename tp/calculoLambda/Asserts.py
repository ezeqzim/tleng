from .Type import *

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

class FreeVariable(Exception):
  pass

def assertTypeBool(expression):
  if (not (expression.type == Arrow(Bool()))):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.type == Arrow(Nat()))):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertTypeLambda(expression):
  if (not (expression.type.right is not None)):
    message = 'La expresion ' + expression.printString() + ' debe ser de tipo Lambda'
    raise ExpressionMustBeLambda(message)

def assertSameType(expression1, expression2):
  if (not (expression1.type == expression2.type)):
    message = 'Las expresiones ' + expression1.printString() + ' y ' + expression2.printString() + ' deben ser del mismo tipo'
    raise ExpressionsMustHaveEqualType(message)

def assertTypeForApplication(expression1, expression2):
  if (not (expression1.vtype == expression2.type)):
    message = 'La expresion ' + expression2.printString() + ' : INSERTAR ALGO ACA no tiene el tipo correcto para aplicarse a ' + expression1.printString() + ' : INSERTAR ALGO ACA'
    raise ExpressionMustBeApplicable(message)
