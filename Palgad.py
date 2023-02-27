from module import*
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    print("1 - Eemalda inimene ja palg, 2 - Lisama uus inimene ja palg, 3 - sorteerimine, 4 - Vordsed palgad")
    a=int(input("Mida teeme: "))
    if a==1:
        udali(palgad,inimesed)
    if a==2:
        dobav(inimesed,palgad)
    if a==3:
        Sorteerimine(inimesed,palgad)
    if a==4:
        Vordsed_palgad(inimesed,palgad)
    else:
        print("Viga")
