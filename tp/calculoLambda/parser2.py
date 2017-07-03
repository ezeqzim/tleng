import ply.yacc as yacc
from .lexer import tokens
from .aux import *
from .aterm import *
from .term import *
from .type import *

# S -> A
def p_s_a(p):
  's : a'
  print 's : a'
  pass

# A -> A L
def p_a_a_l(p):
  'a : a l'
  print 'a : a l'
  pass

# A -> E
def p_a_e(p):
  'a : e'
  print 'a : e'
  pass

# L -> \ var : T . L
def p_l_lambda_v_colon_t_point_l(p):
  'l : LAMBDA v COLON t POINT l'
  print 'l : LAMBDA v COLON t POINT l'
  pass

# L -> E
def p_l_e(p):
  'l : e'
  print 'l : e'
  pass

# T -> Bool F
def p_t_bool_f(p):
  't : BOOL f'
  print 't : BOOL f'
  pass

# T - > Nat F
def p_t_nat_f(p):
  't : NAT f'
  print 't : NAT f'
  pass

# F -> -> T
def p_f_arrow_t(p):
  'f : ARROW t'
  print 'f : ARROW t'
  pass

# F ->
def p_f(p):
  'f : '
  print 'f : '
  pass

# E -> 0
def p_e_zero(p):
  'e : ZERO'
  print 'e : ZERO'
  pass

# E -> true
def p_e_true(p):
  'e : TRUE'
  print 'e : TRUE'
  pass

# E -> false
def p_e_false(p):
  'e : FALSE'
  print 'e : FALSE'
  pass

# E -> V
def p_e_v(p):
  'e : v'
  print 'e : v'
  pass

# E -> if A then L else L
def p_e_if_a_then_l_else_l(p):
  'e : IF a THEN a ELSE a'
  print 'e : IF a THEN l ELSE l'
  pass

# E -> succ ( A )
def p_e_succ_openbracket_a_closedbracket(p):
  'e : SUCC OPENBRACKET a CLOSEDBRACKET'
  print 'e : SUCC OPENBRACKET a CLOSEDBRACKET'
  pass

# E -> pred ( A )
def p_e_pred_openbracket_a_closedbracket(p):
  'e : PRED OPENBRACKET a CLOSEDBRACKET'
  print 'e : PRED OPENBRACKET a CLOSEDBRACKET'
  pass

# E -> iszero ( A )
def p_e_iszero_openbracket_a_closedbracket(p):
  'e : ISZERO OPENBRACKET a CLOSEDBRACKET'
  print 'e : ISZERO OPENBRACKET a CLOSEDBRACKET'
  pass

# E -> ( A )
def p_e_openbracket_a_closedbracket(p):
  'e : OPENBRACKET a CLOSEDBRACKET'
  print 'e : OPENBRACKET a CLOSEDBRACKET'
  pass

# V -> var
def p_v_var(p):
  'v : VAR'
  print 'v : VAR'
  pass

def p_error(p):
  print 'Hubo un error en el parseo'
  raise EOFError
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
