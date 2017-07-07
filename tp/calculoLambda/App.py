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

  def setType(self, atype):
    self.type = atype

  def getApp(self):
    return self.app

  def setApp(self, app):
    self.app = app

  def getExpression(self):
    return self.expression

  def setExpression(self, expression):
    self.expression = expression

  def evaluate(self, context):
    assertNotHasFreeVariables(self.getApp(), context)
    self.setApp(self.getApp().evaluate(context))
    assertTypeArrow(self.getApp())
    assertNotHasFreeVariables(self.getExpression(), context)
    self.setExpression(self.getExpression().evaluate(context))
    assertIsApplicable(self.getApp().getVar(), self.getExpression())
    if (self.getApp().hasFreeVariables({})[0] or self.getExpression().hasFreeVariables({})[0]):
      self.setType(getAppType(self.getApp().getType(), self.getExpression().getType()))
      return self
    return self.getApp().evalWith(self.getExpression(), context)

  def printString(self):
    return self.getApp().printString() + ' ' + self.getExpression().printString()

  def printType(self):
    return self.getType().printType()

  def hasFreeVariables(self, context):
    hasFreeVariables = self.getApp().hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    hasFreeVariables = self.getExpression().hasFreeVariables(context)
    if (hasFreeVariables[0]):
      return (True, hasFreeVariables[1])
    return (False, hasFreeVariables[1])

  def findAndReplace(self, var, parameter):
    self.setApp(self.getApp().findAndReplace(var, parameter))
    self.setExpression(self.getExpression().findAndReplace(var, parameter))
    return self

def getAppType(appType, expType):
  if (expType.right is None):
    if (appType.left == Nat() or appType.left == Bool()):
      return Arrow(appType.left)
    return appType.left
  return getAppType(appType.right, expType.right)
