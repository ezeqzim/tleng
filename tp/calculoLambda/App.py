from .Asserts import *
from .Type import *
from .Var import *
from .Final import *

class App(object):
  def __init__(self, app, expression):
    self.app = app
    self.expression = expression
    self.type = None

  def getType(self):
    return self.type

  def evaluate(self, context):
    assertNotHasFreeVariables(self.app, context)
    self.app = self.app.evaluate(context)
    assertTypeArrow(self.app)
    assertNotHasFreeVariables(self.expression, context)
    self.expression = self.expression.evaluate(context)
    assertIsApplicable(self.app.getVar(), self.expression)
    if (self.app.hasFreeVariables({})[0] or self.expression.hasFreeVariables({})[0]):
      self.type = getAppType(self.app.getType(), self.expression.getType())
      return self
    return self.app.evalWith(self.expression, context)

  def printString(self):
    return self.app.printString() + ' ' + self.expression.printString()

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    hasFreeVariables = self.app.hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.expression.hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    return (False, hasFreeVariables[1])

  def findAndReplace(self, var, parameter):
    self.app = self.app.findAndReplace(var, parameter)
    self.expression = self.expression.findAndReplace(var, parameter)
    return self

def getAppType(appType, expType):
  if (expType.right is None):
    if (appType.left == Nat() or appType.left == Bool()):
      return Arrow(appType.left)
    return appType.left
  return getAppType(appType.right, expType.right)
