from itertools import chain, combinations
Sigma = ['a','b',' ']
S = "q1"
Q = ['q1','q2','q3','q4']
z='A'
RO=['A','B','Z']
F=['q4']
delta = {
        ('q1','a','A'):['q2','AB'],
        ('q1'," ",'A'):['q4',' '],
        ('q2','a','B'):['q2','BB'],
        ('q2','b','B'):['q3',' '],
        ('q3'," ",'A'):['q4','A'],
        ('q3','b','B'):['q3',' ']
    }
stack=['A']
def push(w,stack):
    for s in w:
        stack.append(s)
        
def transicion(estado,sigma):
    global Sigma, delta,stack
    top=stack[-1]
    STATUS = True
    if sigma not in Sigma:
        STATUS = False
        return '',STATUS
    
    if (estado,sigma,top) not in delta.keys():
        STATUS = False
        return '',STATUS
    regreso = delta[(estado,sigma,stack.pop())]
    if regreso[1]!=' ':
        push(regreso[1],stack)
        
    print("Transicion(",estado,",",sigma,",",top,") - >",regreso)     
    return regreso[0],STATUS

#prueba
w=input("Ingrese cadenas de la forma a^n b^n donde n>=0: ")
w=w[:]+' '
#w="aabb "
estado="q1"
for sigma in w:
    estado,STATUS=transicion(estado,sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in F)):
            print (w," si  esta en el lenguaje")
else:print (w," no esta en el lenguaje")