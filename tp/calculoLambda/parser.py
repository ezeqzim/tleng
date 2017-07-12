import ply.yacc as yacc
from .lexer import tokens
from .Start import *
from .Lambda import *
from .ITE import *
from .App import *
from .Final import *
from .Var import *
from .Type import *

# S -> Lambda
def p_s_lambda(p):
  's : lambda'
  p[0] = Start(p[1])

# Lambda -> \ Var : Tipo . Lambda
def p_lambda_lambda_var_colon_tipo_point_lambda(p):
  'lambda : LAMBDA var COLON tipo POINT lambda'
  p[0] = Lambda(p[2], p[4], p[6])

# Lambda -> ITE
def p_lambda_ite(p):
  'lambda : ite'
  p[0] = p[1]

# ITE -> if Lambda then Lambda else Lambda
def p_ite_if_lambda_then_lambda_else_lambda(p):
  'ite : IF lambda THEN lambda ELSE lambda'
  p[0] = IfThenElse(p[2], p[4], p[6])

# ITE -> App
def p_ite_app(p):
  'ite : app'
  p[0] = p[1]

# App -> App Final
def p_app_app_final(p):
  'app : app final'
  p[0] = App(p[1], p[2])

# App -> Final
def p_app_final(p):
  'app : final'
  p[0] = p[1]

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

# Var -> var
def p_var_var(p):
  'var : VAR'
  p[0] = Var(p[1])

# Tipo -> Bool Flecha
def p_tipo_bool_flecha(p):
  'tipo : BOOL flecha'
  if (p[2] is None):
    p[0] = Bool()
  else:
    p[0] = Arrow(Bool(), p[2])

# Tipo - > Nat Flecha
def p_tipo_nat_flecha(p):
  'tipo : NAT flecha'
  if (p[2] is None):
    p[0] = Nat()
  else:
    p[0] = Arrow(Nat(), p[2])

# Tipo -> ( Tipo ) Flecha
def p_tipo_openbracket_tipo_closedbracket_flecha(p):
  'tipo : OPENBRACKET tipo CLOSEDBRACKET flecha'
  if (p[4] is None):
    p[0] = p[2]
  else:
    p[0] = Arrow(p[2], p[4])

# Flecha -> -> Tipo
def p_flecha_arrow_tipo(p):
  'flecha : ARROW tipo'
  p[0] = p[2]

# Flecha ->
def p_flecha(p):
  'flecha : '
  p[0] = None

def p_error(p):
  print 'Hubo un error en el parseo'
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
