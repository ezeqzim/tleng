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
  if (not (expression.getType() == Arrow(Bool()))):
    message = 'La expresion (' + expression.printString() + ' : ' + expression.printType() + ') debe ser de tipo Bool'
    raise ExpressionMustBeBool(message)

def assertTypeNat(expression):
  if (not (expression.getType() == Arrow(Nat()))):
    message = 'La expresion (' + expression.printString() + ' : ' + expression.printType() + ') debe ser de tipo Nat'
    raise ExpressionMustBeNat(message)

def assertTypeArrow(expression):
  if (not (expression.getType().getRight() is not None)):
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
  auxAppType = copy.deepcopy(expression1.getType())
  auxExpType = copy.deepcopy(expression2.getType())
  # auxAppType = typeFlatten(auxAppType)
  # auxExpType = typeFlatten(auxExpType)
  while (auxExpType is not None):
    if (auxAppType is not None and auxAppType.getLeft() == auxExpType.getLeft()):
      auxAppType = auxAppType.getRight()
      auxExpType = auxExpType.getRight()
    else:
      message = 'La expresion (' + expression2.printString() + ' : ' + expression2.printType() + ') no tiene el tipo correcto para aplicarse a (' + expression1.printString() + ' : ' + expression1.printType() + ')'
      raise ExpressionMustBeApplicable(message)
  return auxAppType is not None

def typeFlatten(atype):
  typeList = typeToList(atype)
  res = Arrow(typeList[len(typeList) - 1])
  for i in range(len(typeList) - 2, -1, -1):
    res = Arrow(typeList[i], res)
  return res

def typeToList(atype):
  if (atype is None):
    return []
  if (atype == Bool() or atype == Nat()):
    return [atype]
  return typeToList(atype.getLeft()) + typeToList(atype.getRight())
