from .Asserts import *
from .Type import *
from .Types import *
import copy

class Lambda(object):
  def __init__(self, var, vtype, body):
    var.setType(vtype)
    self.var = var
    self.body = body
    self.type = Arrow(vtype, body.getType())
    self.context = { var.getValue(): vtype }

  def getType(self):
    return self.type

  def setType(self, atype):
    self.type = atype

  def getVar(self):
    return self.var

  def getBody(self):
    return self.body

  def setBody(self, body):
    self.body = body

  def getContext(self):
    return self.context

  def evaluate(self, context):
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    assertNotHasFreeVariables(self.getBody(), auxContext)
    self.setBody(self.getBody().evaluate(auxContext))
    self.setType(Arrow(self.getType().getParam(), self.getBody().getType()))
    return self

  def printString(self):
    return '\\' + self.getVar().printString() + ':' + self.getVar().getType().printString() + '.' + self.getBody().printString()

  def printType(self):
    return self.getType().printType()

  def findAndReplace(self, var, parameter):
    self.setBody(self.getBody().findAndReplace(var, parameter))
    return self

  def hasFreeVariables(self, context):
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    return self.getBody().hasFreeVariables(auxContext)

  def evalWith(self, parameter, context):
    self.getContext().pop(self.getVar().getValue())
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    self.setBody(self.getBody().findAndReplace(self.getVar(), parameter).evaluate(auxContext))
    return self.getBody()
