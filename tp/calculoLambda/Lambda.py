from .Type import *

class Lambda(object):
  def __init__(self, var, vtype, body):
    self.var = var
    self.vtype = vtype
    self.body = body
    self.type = Arrow(vtype, body.type)

  def evaluate(self):
    return self

  def evalWith(self, parameter):
    return self.body.findAndReplace(self.var.value, parameter).evaluate()

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.vtype.printString() + '.' + self.body.printString()

  def printType(self):
    return self.type.printType()
