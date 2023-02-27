#1
def dobav(inimesed,palgad):
    """
    Inimene ja palg lisamine
    """
    cc=int(input("Mitu inimesed tahab lisada: "))
    for i in range(cc):
        a=str(input("Sisestage teie nimi: "))
        if a not in inimesed:    
            c=a.upper()
            zarp=int(input("Sisestage teie palg: "))
            inimesed.append(c)
            palgad.append(zarp)            
        else:
            print("Viga")
    print(palgad,inimesed)
    return inimesed,palgad
    

#2
def udali(palgad,inimesed):
    """
    Eemalda inimese ja palg kriuksumisest
    """
    a=input("Sisestage teie nimi: ")
    if a in inimesed:
        index=inimesed.index(a)
        inimesed.pop(index)
        palgad.pop(index)
        print(inimesed,palgad)
    return palgad,inimesed

#3
def Sorteerimine(inimesed:list,palgad:list):
    v=int(input("palk 1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(palgad)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if palgad[j]<palgad[k]:
                    abi=palgad[j]
                    palgad[j]=palgad[k]
                    palgad[k]=abi
                    abi=inimesed[j]
                    inimesed[j]=inimesed[k]
                    inimesed[k]=abi
                    print()
            
    elif v==2:
        n=len(palgad)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if palgad[j]>palgad[k]:
                    abi=palgad[j]
                    palgad[j]=palgad[k]
                    palgad[k]=abi
                    abi=inimesed[j]
                    inimesed[j]=inimesed[k]
                    inimesed[k]=abi
                    print()
    else:
        print("Viga")
    return inimesed,palgad
#4
def Vordsed_palgad(inimesed:list,palgad:list):
    dublikatid=[x for x in palgad if palgad.count(x)>1]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid:
        n=palgad.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed: ")
        for j in range(n):
            k=palgad.index(palk,k+1)
            nimi=inimesed[k]
            print(nimi)
