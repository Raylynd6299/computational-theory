Sigma=['a','b']
s="q0"
Q=['q0','q1']
F=['q1']
Delta={('q0','a'):['q0','q1'],
        ('q0','b'):['q1'],
        ('q1','b'):['q0','q1']}
from itertools import chain, combinations
def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
Qprima =list(powerset(Q))
Sprima=(s,)
Fprima=[]

print("Qprima")
print(Qprima)

#En Fprima van los miembros de Qprima que contengan a los estados de F

for q in Qprima:
    for x in q:
        if x in F:
            Fprima.append(q)

print("fprima")
print(Fprima)
#construir delta
delta={}

print ("transicion")
for q in Qprima:
    for s in Sigma:
        P=[]
        for x in q:
            if(x,s)in Delta.keys():
                for r in Delta[(x,s)]:
                    if r not in P:
                        P.append(r)
        P.sort()
        print( "(",q,",",s,") ->",tuple(P))
        delta[(q,s)]=tuple(P)
print("delta")
print(delta)


def transicion(estado,sigma):
        global Sigma,delta
        STATUS=True
        if(sigma not in Sigma):
           STATUS=False
           return '',STATUS
        if(estado,sigma) not in delta.keys():
           STATUS=False
           return '',STATUS
        estado_Siguiente=delta[(estado,sigma)]
        print ("Transicion(",estado,',',sigma,")",estado_Siguiente)
        return estado_Siguiente,STATUS

w=input("Ingrese una cadena:  ")
estado=Sprima
for sigma in w:
    estado,STATUS=transicion(estado,sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in Fprima)):
     print (w," si  esta en el lenguaje")
else:print (w," no esta en el lenguaje")