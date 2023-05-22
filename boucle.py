#Exo1
for i in range(1500,2700):
   if i%7==0 and i%5==0:
        print(i ,"est didivible par 7 et multiple de 5")
#Exo2
n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print("")
for i in range(n, 0, -1):
    for j in range(i):
        print("*",end=" ")
    print("")
#Exo3
mot=input("Taper un mot : ")
inverse=""
for i in mot:
    inverse=i+inverse
print("L'inverse du mot",mot,"est",inverse)

#Exo4
nombre=(1,2,3,4,5,6,7,8,9)
pair = 0
impair = 0

for i in nombre:
    if i%2==0:
        pair = pair + 1
    
    elif i%2==1:
        impair = impair + 1

print ("Nombre pair est ", pair)
print ("Nombre pair est ", impair)

