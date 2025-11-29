import re 

class ControleurLumieres:
    def __init__(self, taille=1000): 
        self.taille = taille 
        self.grille_allumage = [[0] * taille for _ in range(taille)]
        self.grille_luminosite = [[0] * taille for _ in range(taille)] 

        self.actions = {
            "activer": self._allumer,
            "désactiver": self._eteindre, 
            "basculer": self._basculer
        }

    def _allumer(self, x, y):
        self.grille_allumage[x][y] = 1 
        self.grille_luminosite[x][y] += 1  # 

    def _eteindre(self, x, y):
        self.grille_allumage[x][y] = 0  
        self.grille_luminosite[x][y] = max(0, self.grille_luminosite[x][y] - 1)  

    def _basculer(self, x, y):
        self.grille_allumage[x][y] = 1 - self.grille_allumage[x][y]
        self.grille_luminosite[x][y] += 2

    def traiter_instructions(self, instructions):
        for ligne in instructions:
            mots = ligne.split()
            if not mots:
                continue 

            action_mot = mots[0]
            if action_mot not in self.actions:
                print(f"Action non reconnue: {action_mot}") 
                continue

            coords = re.findall(r'\d+', ligne)  # coordonnées
            if len(coords) != 4:
                print(f"Format invalide: {ligne}") 
                continue

            x1, y1, x2, y2 = map(int, coords)
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if 0 <= x < self.taille and 0 <= y < self.taille:
                        self.actions[action_mot](x, y)

    def statistiques(self):
        total_allumees = sum(sum(ligne) for ligne in self.grille_allumage)
        luminosite_totale = sum(sum(ligne) for ligne in self.grille_luminosite) 
        return total_allumees, luminosite_totale  

instructions = [ # instruction pour allumer et éteindre
"activer 887,9 à 959,629",
"activer 454,398 à 844,448",
"désactiver 539,243 à 559,965",
"désactiver 370 819 à 676 868",
"désactiver 145,40 à 370,997",
"activer 351 678 à 951 908",
"basculer 720 196 à 897 994",
"basculer 831 394 à 904 860",
]    

controleur = ControleurLumieres()
controleur.traiter_instructions(instructions)
allumees, luminosite = controleur.statistiques()  

print("Nombre de lumières allumées : ", allumees)
print("Luminosité totale :", luminosite) 