from .types import *
from .asserts import *

class App(object):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return self.expression.printString()

class AppList(object):
  def __init__(self, app, expression):
    assertTypeLambda(app)
    assertTypeForApplication(app, expression)
    self.app = app
    self.expression = expression
    self.value = app.value(expression.value)
    self.type = afterApplicationType(app.type, expression.type)

  def printString(self):
    return '(' + self.app.printString() + ') ' + self.expression.printString()

class Enclosed(Term):
  def __init__(self, expression):
    self.expression = expression
    self.value = expression.value
    self.type = expression.type

  def printString(self):
    return '(' + self.expression.printString() + ')'
