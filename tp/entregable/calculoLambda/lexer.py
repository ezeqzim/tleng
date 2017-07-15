#! coding: utf-8
import ply.lex as lex

class UnexpectedTokenException(Exception):
  pass

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'Bool' : 'BOOL',
   'Nat' : 'NAT',
   'succ' : 'SUCC',
   'pred' : 'PRED',
   'iszero' : 'ISZERO',
   'true' : 'TRUE',
   'false' : 'FALSE',
}

tokens = [
  'VAR',
  'LAMBDA',
  'COLON',
  'POINT',
  'ZERO',
  'OPENBRACKET',
  'CLOSEDBRACKET',
  'ARROW'
] + list(reserved.values())

t_LAMBDA = r'\\'
t_COLON = r':'
t_POINT = r'\.'
t_ZERO = r'0'
t_OPENBRACKET = r'\('
t_CLOSEDBRACKET = r'\)'
t_ARROW = r'->'

t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_BOOL = r'Bool'
t_NAT = r'Nat'
t_SUCC = r'succ'
t_PRED = r'pred'
t_ISZERO = r'iszero'
t_TRUE = r'true'
t_FALSE = r'false'

t_ignore = ' \t'

def t_VAR(token):
  r'[a-z][a-zA-Z]*'
  if token.value in reserved:
    token.type = reserved[token.value]
    token.value = reserved[token.value]
  return token

def t_error(token):
  message = 'Token desconocido: ' + str(token.value)
  raise UnexpectedTokenException(message)

lexer = lex.lex()

def apply_lexer(string):
  lexer.input(string)
  return list(lexer)
