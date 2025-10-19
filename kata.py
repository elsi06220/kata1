import re

grille_allumage = [[0] * 1000 for _ in range(1000)]       # 1 
grille_luminosite = [[0] * 1000 for _ in range(1000)]     # 2 

instructions = [
    "activer 887,9 à 959,629",
    "activer 454 398 à 844 448",
    "désactiver 539 243 à 559 965",
    "désactiver 370 819 à 676 868",
    "désactiver 145,40 à 370,997",
    "désactiver 301,3 à 808,453",
    "activer 351 678 à 951 908",
    "basculer 720 196 à 897 994",
    "basculer 831 394 à 904 860"
]

for ligne in instructions:
    if ligne.startswith("activer"):
        action = "allumer"
    elif ligne.startswith("désactiver"):
        action = "eteindre"
    elif ligne.startswith("basculer"):
        action = "basculer"

    
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', ligne))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "allumer":
                grille_allumage[x][y] = 1
            elif action == "eteindre":
                grille_allumage[x][y] = 0
            elif action == "basculer":
                grille_allumage[x][y] = 1 - grille_allumage[x][y]
           

            if action == "allumer":
                grille_luminosite[x][y] += 1
            elif action == "eteindre":
                grille_luminosite[x][y] = max(0, grille_luminosite[x][y] - 1)
            elif action == "basculer":
                grille_luminosite[x][y] += 2
           


total_allumees = sum(sum(ligne) for ligne in grille_allumage)
luminosite_totale = sum(sum(ligne) for ligne in grille_luminosite)

print("Nombre de lumières allumées :", total_allumees)
print("Luminosité totale :", luminosite_totale)
