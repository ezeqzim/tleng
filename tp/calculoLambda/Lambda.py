from .Asserts import *
from .Type import *
from .Types import *

class Lambda(object):
  def __init__(self, var, vtype, body):
    var.setType(vtype)
    self.var = var
    self.vtype = vtype
    self.body = body
    self.type = Arrow(vtype, body.getType())
    self.context = {var.getValue(): vtype}

  def getType(self):
    return self.type

  def evaluate(self, context):
    self.context.update(context)
    if (self.body.hasFreeVariables(self.context)):
      self.body.printType() # raise FreeVariable
    self.body = self.body.evaluate(self.context)
    return self

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.vtype.printString() + '.' + self.body.printString()

  def printType(self):
    return self.type.printType()

  def hasFreeVariables(self, context):
    context.update(self.context)
    return self.body.hasFreeVariables(context)

  def evalWith(self, parameter, context):
    assertTypeForApplication(self.var, parameter)
    self.context.pop(self.var.getValue())
    replaced = self.body.findAndReplace(self.var, parameter)
    self.context.update(context)
    return replaced.evaluate(self.context)
