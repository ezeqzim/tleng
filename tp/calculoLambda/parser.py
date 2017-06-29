import ply.yacc as yacc
from .lexer import tokens

enable_debug = True
# enable_debug = False

# Term -> App
def p_term_app(p):
  'term : app'
  if(enable_debug):
    print 'term : app'
  p[0] = p[1]

# Term -> succ(Term)
def p_term_succ_openbracket_term_closedbracket(p):
  'term : SUCC OPENBRACKET term CLOSEDBRACKET'
  if(enable_debug):
    print 'term : SUCC OPENBRACKET term CLOSEDBRACKET'
  p[0] = p[3] + 1

# Term -> pred(Term)
def p_term_pred_openbracket_term_closedbracket(p):
  'term : PRED OPENBRACKET term CLOSEDBRACKET'
  if(enable_debug):
    print 'term : PRED OPENBRACKET term CLOSEDBRACKET'
  p[0] = p[3] - 1 if (p[3] > 0) else p[3]

# Term -> iszero(Term)
def p_term_iszero_openbracket_term_closedbracket(p):
  'term : ISZERO OPENBRACKET term CLOSEDBRACKET'
  if(enable_debug):
    print 'term : ISZERO OPENBRACKET term CLOSEDBRACKET'
  p[0] = p[3] == 0

# Term -> if Term then Term else Term
def p_term_if_term_then_term_else_term(p):
  'term : IF term THEN term ELSE term'
  if (enable_debug):
    print 'term : IF term THEN term ELSE term'
  p[0] = p[4] if p[2] else p[6]

# Term -> \var:T.Term
def p_term_lambda_var_colon_type_point_term(p):
  'term : LAMBDA VAR COLON type POINT term'
  if(enable_debug):
    print 'term : LAMBDA VAR COLON type POINT term'
  p[0] = p[1]

# Term -> (Term)
def p_term_openbracket_term_closedbracket(p):
  'term : OPENBRACKET term CLOSEDBRACKET'
  if (enable_debug):
    print 'term : OPENBRACKET term CLOSEDBRACKET'
  p[0] = p[2]

# App -> ATerm
def p_app_aterm(p):
  'app : aterm'
  if(enable_debug):
    print 'app : aterm'
  p[0] = p[1]

# App -> App ATerm
def p_app_app_aterm(p):
  'app : app aterm'
  if(enable_debug):
    print 'app : app aterm'
  p[0] = p[1]

# ATerm -> 0
def p_aterm_0(p):
  'aterm : ZERO'
  if(enable_debug):
    print 'aterm : ZERO'
  p[0] = p[1]

# ATerm -> true
def p_aterm_true(p):
  'aterm : TRUE'
  if(enable_debug):
    print 'aterm : TRUE'
  p[0] = p[1]

# ATerm -> false
def p_aterm_false(p):
  'aterm : FALSE'
  if(enable_debug):
    print 'aterm : FALSE'
  p[0] = p[1]

# ATerm -> var
def p_aterm_var(p):
  'aterm : VAR'
  if(enable_debug):
    print 'aterm : VAR'
  p[0] = p[1]

# Type -> Bool Arrow
def p_type_bool_arrow(p):
  'type : BOOL arrow'
  if (enable_debug):
    print 'type : BOOL arrow'
  p[0] = p[1]

# Type -> Nat Arrow
def p_type_nat_arrow(p):
  'type : NAT arrow'
  if (enable_debug):
    print 'type : NAT arrow'
  p[0] = p[1]

# Arrow -> -> Type
def p_arrow_arrow_type(p):
  'arrow : ARROW type'
  if (enable_debug):
    print 'arrow : ARROW type'
  p[0] = p[1] + p[2]

# Arrow ->
def p_arrow(p):
  'arrow : '
  if (enable_debug):
    print 'arrow : '
  pass

def p_error(p):
  print("Hubo un error en el parseo.")
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
