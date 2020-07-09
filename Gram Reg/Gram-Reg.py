tokens = ('a','b')
t_a = r'a'
t_b = r'b'
def t_error (t):
    print ("Caracter ilegal '%s' " % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex 
lex.lex()

def p_S(p):
    '''S : b A
         | empty '''
    pass

def p_A(p):
    ''' A : a a A
          | b
          | empty  '''
    pass
def p_empty(p):
    ''' empty : '''
    pass
w=''
def p_error(p):
    global w
    if p:
        print("Error de la sintaxis en '%s'"% p.value)
        print(w,"no esta en el lenguaje")
    else: 
        print("Error de sintaxis en EOF")
        print(w, "no esta en el lenguaje")

import  ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        w= input('>')
    except EOFError:
        break
    t=yacc.parse(w)
