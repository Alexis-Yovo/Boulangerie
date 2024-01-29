print("Que voulez-vous acheter ?")
print("Les prix de nos différents articles: \n Baguette : 1.80, Croissant: 0.85 , Pain au Chocolat : 0.85, Chausson aux Pommes:0.85 ")
argent = 10
baguette = 1.80
croissant = 0.85
pain_chocolat = 0.85
chausson_pommes = 0.85
reste = 0

choix = input("Je voudrais prendre l'article : ")
quantite = int(input("Combien ?"))
monnaie = int(input("Entrez votre monnaie : "))  # Ajout d'une variable pour stocker la monnaie

# Utilisation correcte des conditions pour vérifier si l'utilisateur peut acheter l'article choisi
if (choix == "baguette") and (argent >= baguette * quantite):
   produit = quantite * baguette
   reste = monnaie - produit
   print("Vous avez acheté " + str(quantite) + " baguette(s) pour " + str(produit) + "€")
   print("Je vous rends " + str(reste) + "€")
elif (choix == "croissant") and (argent >= croissant * quantite):
   produit = quantite * croissant
   reste = monnaie - produit
   print("Vous avez acheté " + str(quantite) + " croissant(s) pour " + str(produit) + "€")
   print("Je vous rends " + str(reste) + "€")
elif (choix == "pain_chocolat") and (argent >= pain_chocolat * quantite):
   produit = quantite * pain_chocolat
   reste = monnaie - produit
   print("Vous avez acheté " + str(quantite) + " pain(s) au chocolat pour " + str(produit) + "€")
   print("Je vous rends " + str(reste) + "€")
elif (choix == "chausson_pommes") and (argent >= chausson_pommes * quantite):
   produit = quantite * chausson_pommes
   reste = monnaie - produit
   print("Vous avez acheté " + str(quantite) + " chausson(s) aux pommes pour " + str(produit) + "€")
   print("Je vous rends " + str(reste) + "€")
else:
   print("Vous n'avez pas assez d'argent ou l'article choisi n'est pas disponible")
