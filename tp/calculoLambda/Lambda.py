from .Asserts import *
from .Type import *
from .Types import *

class Lambda(object):
  def __init__(self, var, vtype, body):
    self.var = var
    self.vtype = vtype
    self.body = body
    self.type = Arrow(vtype, body.getType())
    self.context = {var.value: vtype}

  def getType(self):
    return self.type

  def evaluate(self, context):
    self.context.update(context)
    if (self.body.hasFreeVariables(self.context)):
      self.body.printType() # raise FreeVariable
    return Lambda(self.var, self.vtype, self.body.evaluate(self.context))

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.vtype.printString() + '.' + self.body.printString()

  def printType(self):
    return self.type.printType()

  def hasFreeVariables(self, context):
    context.update(self.context)
    return self.body.hasFreeVariables(context)

  def evalWith(self, parameter, context):
    assertTypeForApplication(self.var, parameter)
    self.context.pop(self.var)
    replaced = self.body.findAndReplace(self.var, parameter)
    return replaced.evaluate(self.context.update(context))
