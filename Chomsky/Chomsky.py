E=['a','b','d']
G={'S':['Aa','B','D'],
   'B':['b'],
   'A':['aA','bA','B'],
   'C':['abd']}
Gprime={}
G2prime={'S':[]}
G3prime={}
G4prime={}
G6prime={}
def p1(G,Gprime):
    for a in G.keys():
        for x in G[a]:
            if x.islower():
                if a in Gprime.keys():
                    Gprime[a].append(x)
                    G[a].remove(x)
                else:
                    Gprime[a]=[x]
                    G[a].remove(x)
def p2(G,Gprime):
    p=0
    f=0
    while(f!=(p+2)):
        if(Gprime.keys()==G.keys()):
            f+=1
        else:
            p+=1
            f+=1
        for k in G.keys():#recorrera todas las llaves de G
            if k in Gprime.keys():#si k esta en las llaves de Gprime
                for c in G[k]:
                    for i,v in enumerate(c):
                        if (v in E) or (v in Gprime.keys()):
                            if i+1==len(c): 
                                Gprime[k].append(c)
                                G[k].remove(c)
                        else:
                            break;
            else:
                for c in G[k]:
                    for i,v in enumerate(c):
                        if (v in E) or (v in Gprime.keys()):
                            if i+1==len(c):
                                if k in Gprime.keys():
                                    Gprime[k].append(c)
                                    G[k].remove(c)
                                else:
                                    Gprime[k]=[c]
                                    G[k].remove(c)
                        else:
                            break;
def p3 (Gprime,G2prime):
    Eprime=[]
    Nprime=['S']
    for a in Nprime:
        for x in Gprime[a]:
            G2prime[a].append(x)
            for c in x:
                if c.islower():
                    if c not in Eprime:
                        Eprime.append(c)
                else:
                    if c not in G2prime.keys():
                        G2prime[c]=[]
                        Nprime.append(c)
def p4(G,Gprime):
    Ns=[]
    def evalk(k):
        global G,Ns
        for c in G[k]:
            if len(c)==1:
                if c in G.keys():
                    if evalk(c)==1:
                        if(k not in Ns):
                            Ns.append(k)
                elif (c=='~'):
                    if (k not in Ns ):
                        Ns.append(k)
                    return 1
                else:
                    return 0
            elif c.isupper():
                for x in c:
                    evalk(x)            
    for k in G.keys():
        evalk(k)
    for x in G.keys():
        for c in G[x]:
            if not(c=='~'):
                if c.islower():
                    if x in Gprime.keys():
                        if c not in Gprime[x]:
                            Gprime[x].append(c)
                    else:
                        
                            Gprime[x]=[c]
                elif c.isupper():
                    f=0
                    for i,l in enumerate(c):
                        if l in Ns:
                            p=c[:i]+c[i+1:]
                            if x in Gprime.keys():
                                f+=1
                                if c not in Gprime[x]:
                                    Gprime[x].append(c)
                                if (len(p)>0):
                                    if p not in Gprime[x]:
                                        Gprime[x].append(p)
                            else:
                                f+=1
                                Gprime[x]=[c]
                                if (len(p)>0):
                                    Gprime[x].append(p)
                        else:
                            if x in Gprime.keys():
                                if len(c)-1==f:
                                    if c not in Gprime[x]:
                                        Gprime[x].append(c)
                            else:
                                if len(c)-1==f:
                                    Gprime[x]=[c]
                        if len(c)-1==i:
                            f=0
                        f+=1
                        
                else:
                    f=0
                    for i,l in enumerate(c):
                        if l in Ns:
                            p=c[:i]+c[i+1:]
                            if x in Gprime.keys():
                                f+=1
                                if c not in Gprime[x]:
                                    Gprime[x].append(c)
                                if (len(p)>0):
                                    if p not in Gprime[x]:
                                        Gprime[x].append(p)
                            else:
                                f+=1
                                Gprime[x]=[c]
                                if (len(p)>0):
                                    Gprime[x].append(p)
                        else:
                            if x in Gprime.keys():
                                if len(c)-1==f:  
                                    Gprime[x].append(c)
                            else:
                                if len(c)-1==f:
                                    Gprime[x]=[c]
                                    
                        if len(c)-1==i:
                            f=0
                        f+=1
    for x in G['S']:
        if (x=='~'):
            Gprime['S'].append('~')
        elif(x.isupper()):
            f=1
            for i,l in enumerate(c):
                if l in Ns:
                    f+=1
            if f==len(c):
                Gprime['S'].append('~')
def p5(G,Gprime):
    U={}
    def unit(G,k,U):
        for x in G[k]:
            if k not in U.keys():
                U[k]=[k]            
            if len(x)==1 and x.isupper() and (x in G.keys()):
                if x not in U[k]:
                    U[k].append(x)
                unit(G,x,U)
                if x in U.keys():
                    for h in U[x]:
                        if h not in U[k]:
                             U[k].append(h)
    for k in G.keys():
        unit(G,k,U)
    for x in U.keys():
        if len(U[x])>1:
            for c in U[x]:
                for k in G[c]:
                    if k not in U[x]:
                        if x not in Gprime.keys():
                            Gprime[x]=[k]
                        else:
                            if k not in Gprime[x]:
                                Gprime[x].append(k)
    for x in G.keys():
        for k in G[x]:
            if k not in U.keys():
                if x not in Gprime.keys():
                    Gprime[x]=[k]
                else:
                    if k not in Gprime[x]:
                        Gprime[x].append(k)
                        
def ch(G,G2p):
    Gprime={}
    n=1
    for x in G.keys():
        for c in G[x]:
            cs=list(c)
            for i,l in enumerate(cs):
                if l.islower():
                    s='C'+ str(n)
                    n+=1
                    cs[i]=s
                    if s not in Gprime.keys():
                        Gprime[s]=[l]      
                if i==len(c)-1:
                    
                    if x not in Gprime.keys():
                        Gprime[x]=[cs]
                    else:
                        Gprime[x].append(cs)
    d=0
    for x in Gprime.keys():
        for c in Gprime[x]:
            cs=list(c)
            if len(c)>1:
                for i,l in enumerate(cs):
                    if i%2==0:
                        g='D'+ str(d)
                        d+=1
                        f=cs[:i+1]
                        if len(f)>2:
                            while(len(f)>2):
                                f=f[1:]
                        if i!=len(cs)-1:
                            f.append(g)
                        if x not in G2p.keys():
                            l=""
                            for z in f:
                                l+=z
                            G2p[x]=[l]
                        else:
                            l=""
                            for z in f:
                                l+=z
                            G2p[g]=[l] 
            else:
                G2p[x]=[c]

p1(G,Gprime)
p2(G,Gprime)
p3(Gprime,G2prime)
p4(G2prime,G3prime)#nota epsilon se marca como '~'
p5(G3prime,G4prime)
G5prime={'S':[]}
p3(G4prime,G5prime)#le vuelvo a aplicar el de quitar simbolos inutiles
ch(G5prime,G6prime)
print("G': ",Gprime) 
print("G'' : ",G2prime)
print("G''': ",G3prime)
print("G'''': ",G5prime)
print("G''''': ",G6prime)