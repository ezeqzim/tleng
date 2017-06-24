#! coding: utf-8
import ply.lex as lex

tokens = (
#  'VAR',
  'TRUE',
  'FALSE',
  'IF',
  'THEN',
  'ELSE',
  'LAMBDA',
  'COLON',
  'POINT',
  'ZERO',
  'SUCC',
  'PRED',
  'ISZERO',
  'OPENBRACKET',
  'CLOSEDBRACKET',
  'TBOOL',
  'TNAT',
  'TARROW'
)

#t_VAR = r'[a-z][a-z0-9]*'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_LAMBDA = r'\\'
t_COLON = r':'
t_POINT = r'\.'
t_SUCC = r'succ'
t_PRED = r'pred'
t_ISZERO = r'iszero'
t_OPENBRACKET = r'\('
t_CLOSEDBRACKET = r'\)'
t_TBOOL = r'Bool'
t_TNAT = r'Nat'
t_TARROW = r'->'
t_ignore = ' \t'

def t_TRUE(t):
  r'true'
  t.value = True
  return t

def t_FALSE(t):
  r'false'
  t.value = False
  return t

def t_ZERO(t):
  r'0'
  t.value = 0
  return t

lexer = lex.lex()

def apply_lexer(string):
  lexer.input(string)
  return list(lexer)
