#1
def dobav(inimesed,palgad):
    """
    Inimene ja palg lisamine
    """
    cc=int(input("Mitu inimesed tahab lisamine"))
    for i in range(cc):
        a=str(input("Sisestage teie nimi: "))
        if a not in inimesed:    
            c=a.upper()
            zarp=str(input("Sisestage teie palg: "))
            vv=inimesed.append(zarp)
            cc=palgad.append(c)            
        else:
            print("Viga")
    print(palgad,inimesed)
    return cc,vv
    

#2
def udali(palgad,inimesed):
    """
    Eemalda inimese ja palg kriuksumisest
    """
    a=input("Sisestage inimene millest tahab eemalda: ")
    b=input("Sisestage Palg millest tahab eemalda: ")
    a=a.upper()
    aa=inimesed.remove(a)
    bb=palgad.remove(b)
    print(palgad, inimesed)
    return aa,bb
