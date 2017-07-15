from .Type import *
from .Types import *
import copy

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
  if (not (expression.getType() == Bool())):
    message = 'La expresion (' + expression.printString() + ' : ' + expression.printType() + ') debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.getType() == Nat())):
    message = 'La expresion (' + expression.printString() + ' : ' + expression.printType() + ') debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertTypeArrow(expression):
  if (expression.getType() == Bool() or expression.getType() == Nat()):
    message = 'La expresion (' + expression.printString() + ' : ' + expression.printType() + ') debe ser de tipo Arrow'
    raise ExpressionMustBeLambda(message)

def assertSameType(expression1, expression2):
  if (not (expression1.getType() == expression2.getType())):
    message = 'Las expresiones (' + expression1.printString() + ' : ' + expression1.printType() + ') y (' + expression2.printString() + ' : ' + expression2.printType() + ') deben ser del mismo tipo'
    raise ExpressionsMustHaveEqualType(message)

def assertTypeNonVar(expression):
  if (expression.getType() is None):
    message = 'La variable ' + expression.getValue() + ' esta libre'
    raise FreeVariable(message)

def assertNotHasFreeVariables(expression, context):
  hasFreeVariables = expression.hasFreeVariables(context)
  if (hasFreeVariables[0]):
    assertTypeNonVar(hasFreeVariables[1])

def assertIsApplicable(expression1, expression2):
  if (not (expression1.getType().getParam() == expression2.getType())):
    message = 'La expresion (' + expression2.printString() + ' : ' + expression2.printType() + ') no tiene el tipo correcto para aplicarse a (' + expression1.printString() + ' : ' + expression1.printType() + ')'
    raise ExpressionMustBeApplicable(message)
