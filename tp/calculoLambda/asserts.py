from .types import *

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
  if (not (expression.type == Types.BOOL)):
    message = 'La expresion ' + str(expression.value) + ' debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.type == Types.NAT)):
    message = 'La expresion ' + str(expression.value) + ' debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertTypeLambda(expression):
  if (not (expression.type == Types.LAMBDA)):
    message = 'La expresion ' + str(expression.value) + ' debe ser de tipo Lambda'
    raise ExpressionMustBeLambda(message)

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
