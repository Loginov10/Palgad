from module import*
palgad=["1200","2500","750","395","1200"]
inimesed=["A","B","C","D","E"]
while True:
    print("1 - Eemalda inimene ja palg, 2 - Lisama uus inimene ja palg")
    a=int(input("Mida teeme: "))
    if a==1:
        udali(palgad,inimesed)
    if a==2:
        dobav(palgad,inimesed)
    
    else:
        print("Viga")