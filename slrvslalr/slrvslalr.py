# -----------------------------------------------------------------------------
# slrvslalr.py
#
# VICTORIA VELASCO TATE
# 217031118
# -----------------------------------------------------------------------------


#   ANÁLISE LÉXICA ----------------------------------------------

#   TOKENS 
tokens = ('ID','EQUALS', 'STAR')

t_STAR   = r'\*'
t_EQUALS = r'='
t_ID     = r'id'

#   IGNORANDO ESPAÇOS E TABS
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
#   VALIDANDO CARACTERES LIDOS DE ACORDO COM OS TOKENS MAPEADOS
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
        



#   ANÁLISE SINTÁTICA ------------------------------------------

#   DEFININDO A GRAMÁTICA
def p_expression(t):
    ''' 
        S : L EQUALS R
          | R  
        L : STAR R
          | ID
        R : L
          
    '''
    if   t[1] == '='  : t[0] = t[2]
    elif t[1] == '*'  : t[0] = t[2]
    elif t[1] == 'id' : t[0] = ''
    else              : t[0] = t[1]

#   VALIDANDO PROBLEMAS DE SINTAXE
def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
import ply.lex as lex

lexer   = lex.lex()

#   DEFININDO MÉTODO UTILIZADO
op = input('Escolha o método: \n [1] SLR \n [2] LALR \n -> ')
if op == '1'  :   parser = yacc.yacc(method='SLR')
else          :   parser = yacc.yacc(method)


#   RECEBENDO INPUT PARA ANÁLISE
while True:
    try:
        s = input('S -> ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
