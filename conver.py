from datetime import*
dateact=date.today()
heure=datetime.time(datetime.now())
print(dateact)
print(heure)
print("Année en cours : ",dateact.year)
mois=dateact.month
lesmois=["Janvier","Férier","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novenbre","Décembre"]

print("mois de année : ",lesmois[mois-1])

print("numero de la semaine : ",dateact.strftime("%W"))

print("jour de la semaine : ",date.weekday(dateact)+1)
jour=date.weekday(dateact)
jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

print("jour de la semaine : ",jours[jour])
print("jour de l'année  : ",dateact.strftime("%j"))
print("jour du mois : ",dateact.strftime("%d"))

def convert(date):
    format = "%b %d %Y %I:%M%p" 
    datet = datetime.datetime.strptime(date, format)
 
    return datet
 

date = "jan 1 2014 02:43PM"
print(convert(date))