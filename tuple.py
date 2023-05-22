#EXO1
print("EXO1")
t=()
print(t)
tup=(1,4,8,'voiture',2,'moto',5)
print(tup)
t2= 1,3,4,'t'
print(t2)

#EXO2
print("EXO2")
tup=(1,4,8,'voiture',2,'moto',5)
print (tup[3])
print (tup[3:-1])

#EXO3
print("EXO3")
tup=(1,4,8,'voiture',2,'moto',5)
if 'voiture'in tup:
    print("oui")
else:
    print("non")
#Autre methode
i=input("Entrez i : ")
if i in tup:
    print(i,'est dans tup')
else:
    print('Non')

#Exo4
print("EXO4")
tupl=('nom','diawara'),('prenom','tata')
print(tupl)
print(dict(tupl))
#2e methode
def conv(dic,tup):
    d=dict(tup)
    return d
tup=('nom','diawara'),('prenom','tata')
dic={}
print(conv(dic,tup))
