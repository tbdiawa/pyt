
numsecurite=str(input("Entrer votre numéro de sécurité sociale (13 chiffres) --> "))
chiffre=int(numsecurite)
if len(numsecurite)==13:

    cle=str(input("Entrer votre clé de contrôle (2 chiffres) ----> "))
    clesec=int(cle)
    if len(cle)==2:

        if clesec== 97 - (chiffre % 97):
            print("Votre numéro de sécurité sociale est valide.")
        else:
            print("Votre numéro de sécurité sociale est INVALIDE !")
    else:
        print("clé de controle invalide ")
else:
    print("numero invalide ")       