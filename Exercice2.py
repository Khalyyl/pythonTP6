class Voiture():

    def __init__(self,marque="ford",couleur="rouge",pilote="personne",vitesse=0):
        self.marque=marque
        self.couleur=couleur
        self.pilote=pilote
        self.vitesse=vitesse

    def Choix_conducteur(self, nom):
        self.nom=nom
    def accelerer(self, taux,duree):
        self.taux=taux
        self.duree=duree
        Voiture.vitesse=taux*duree

    def afficher_tout(self):
        print(f"Maque :{self.marque} 
              --Nom: {self.nom} -- Couleur : {self.couleur}  ")

if __name__== "__main__":
    a1=Voiture('Peugeot','bleue')
    a2=Voiture(couleur='verte')
    


        