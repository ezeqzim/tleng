import ply.yacc as yacc
from .lexer import tokens
from .Start import *
from .Lambda import *
from .App import *
from .Final import *
from .Type import *
from .Var import *

# S -> Lambda
def p_s_lambda(p):
  's : lambda'
  p[0] = Start(p[1])

# Lambda -> App
def p_lambda_app(p):
  'lambda : app'
  p[0] = Lambda(p[1])

# App -> App Final
def p_app_app_final(p):
  'app : app final'
  p[0] = AppList(p[1], p[2])

# App -> Final
def p_app_final(p):
  'app : final'
  p[0] = App(p[1])

# Final -> 0
def p_final_zero(p):
  'final : ZERO'
  p[0] = Zero()

# Final -> true
def p_final_true(p):
  'final : TRUE'
  p[0] = FTrue()

# Final -> false
def p_final_false(p):
  'final : FALSE'
  p[0] = FFalse()

# Final -> Var
def p_final_var(p):
  'final : var'
  p[0] = p[1]

# Final -> if Lambda then Lambda else Lambda
def p_final_if_lambda_then_lambda_else_lambda(p):
  'final : IF lambda THEN lambda ELSE lambda'
  p[0] = IfThenElse(p[2], p[4], p[6])

# Final -> succ ( Lambda )
def p_final_succ_openbracket_lambda_closedbracket(p):
  'final : SUCC OPENBRACKET lambda CLOSEDBRACKET'
  p[0] = Succ(p[3])

# Final -> pred ( Lambda )
def p_final_pred_openbracket_lambda_closedbracket(p):
  'final : PRED OPENBRACKET lambda CLOSEDBRACKET'
  p[0] = Pred(p[3])

# Final -> iszero ( Lambda )
def p_final_iszero_openbracket_lambda_closedbracket(p):
  'final : ISZERO OPENBRACKET lambda CLOSEDBRACKET'
  p[0] = Iszero(p[3])

# Final -> ( Lambda )
def p_final_openbracket_lambda_closedbracket(p):
  'final : OPENBRACKET lambda CLOSEDBRACKET'
  p[0] = Enclosed(p[2])

# Final -> \ Var : Tipo . Lambda
def p_final_lambda_var_colon_tipo_point_lambda(p):
  'final : LAMBDA var COLON tipo POINT lambda'
  p[0] = Abstraction(p[2], p[4], p[6])

# Tipo -> Bool Flecha
def p_tipo_bool_flecha(p):
  'tipo : BOOL flecha'
  p[0] = Arrow(Bool(p[1]), p[2])

# Tipo - > Nat Flecha
def p_tipo_nat_flecha(p):
  'tipo : NAT flecha'
  p[0] = Arrow(Nat(p[1]), p[2])

# Flecha -> -> Tipo
def p_flecha_arrow_tipo(p):
  'flecha : ARROW tipo'
  p[0] = Arrow(p[2])

# Flecha ->
def p_flecha(p):
  'flecha : '
  pass

# Var -> var
def p_var_var(p):
  'var : VAR'
  p[0] = Var(p[1])

def p_error(p):
  print 'Hubo un error en el parseo'
  raise EOFError
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
