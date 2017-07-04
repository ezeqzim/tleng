from .Asserts import *

class App(object):
  def __init__(self, app, expression):
    self.app = app
    self.expression = expression
    self.type = Arrow(app.type, expression.type) # ESTE ES FRUTA PARA PROBAR

  def evaluate(self):
    resApp = self.app.evaluate()
    assertTypeLambda(resApp)
    resExpression = self.expression.evaluate()
    assertTypeForApplication(resApp, resExpression)
    return resApp.evalWith(resExpression)

  def printString(self):
    return self.app.printString() + ' ' + self.expression.printString()
