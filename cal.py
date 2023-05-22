conso=0
num=str
date=str
op=str
tarifnat=int
tarifint=int
credit=int
solde=0





while(True):
    print("--------------------")
    print("|      MENU        |")
    print("|------------------|")
    print("| 1.Initialiser    |")
    print("| 2.Fiche SIM      |")
    print("| 3.Créditer       |")
    print("| 4.Appel          |")
    print("| 5.Solde          |")
    print("| 0.Quitter        |")
    print("|------------------|")
    choix=int(input("Choix : "))


    if choix==1:
        print("Initialiser : ")
        num=str(input("Numéro téléphone : "))
        date=str(input("Date d'achat : ")) 
        op=str(input("Opérateur : "))
        tarifnat=int(input("Tarif national : "))
        tarifint=int(input("Tarif international : "))


    elif choix==2:
        print("Fiche SIM ")
        print("------------")
        print(num)
        print(op)
        print(date)

    
    elif choix==3:
        print("Créditer : ")
        credit=int(input("Crédit : "))
        solde=solde+credit


    elif choix==4:
        print("Appel  : ")
        appel=str(input("type d'appel : "))
        nbM=float(input("Durée : "))
        
      
        if appel== "national":
             conso=nbM*tarifnat
             solde=credit-conso
             print(solde)

        elif appel=="international":
            conso=nbM*tarifint
            solde=solde-conso
            print(solde)       
     
    elif choix==5:
        print("Solde : ")
        solde=solde
        print(solde)
        

    elif choix==0:
        print("bye bye! ")
        break
