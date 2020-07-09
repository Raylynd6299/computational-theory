#Estados inicial
Q=["q0","q1","q2"]
S="q0"
Sigma=['a','b']
F=['q1']
delta={('q0','a'):'q0',('q0','b'):'q1',('q1','a'):'q2',('q1','b'):'q2',('q2','a'):'q2',('q2','b'):'q2'}
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
#Prueba
#w=input("Ingrese la cadena a evaluar: ")
w= raw_input("Ingrese la cadena: ")
estado=S
for sigma in w:
    estado,STATUS=transicion(estado,sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in F)):
            print (w," si  esta en el lenguaje")
else:print (w," no esta en el lenguaje")
    


