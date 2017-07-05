from .Asserts import *
from .Type import *
from .Var import *

class App(object):
  def __init__(self, app, expression):
    self.app = app
    self.expression = expression
    self.type = None

  def getType(self):
    return self.type

  def evaluate(self, context):
    if (self.app.hasFreeVariables(context)):
      self.app.printType() # raise FreeVariable
    resApp = self.app.evaluate(context)
    assertTypeLambda(resApp)
    if (self.expression.hasFreeVariables(context)):
      self.expression.printType() # raise FreeVariable
    resExpression = self.expression.evaluate(context)
    if (self.app.hasFreeVariables({}) or self.expression.hasFreeVariables({})):
      self.type = Arrow(self.app.getType().left)
      return self
    return resApp.evalWith(resExpression, context)

  def printString(self):
    return '(' + self.app.printString() + ' ' + self.expression.printString() + ')'

  def printType(self):
    return '(' + self.getType().printType() + ')'

  def hasFreeVariables(self, context):
    return self.app.hasFreeVariables(context) or self.expression.hasFreeVariables(context)

  def findAndReplace(self, var, parameter):
    return App(self.app.findAndReplace(var, parameter), self.expression.findAndReplace(var, parameter))
