class Voiture():

    def __init__(self,marque="ford",couleur="rouge",pilote="personne",vitesse=0):
        self.marque=marque
        self.couleur=couleur
        self.pilote=pilote
        self.vitesse=vitesse
    
    def __str__(self):
        return(f"Marque :{self.marque}, Couleur :{self.couleur}, Pilote :{self.pilote}, Vitesse :{self.vitesse}")


    def Choix_conducteur(self, nom):
        self.pilote=nom
    
    def accelerer(self, taux,durée):
        if self.pilote != 'personne':
           gain_vitesse=taux*durée
           self.vitesse = self.vitesse + gain_vitesse
    
    def afficher_tout(self):
        print(f"La voiture {self.marque} de couleur {self.couleur} est piloté par {self.pilote} avec un vitesse {self.vitesse}")

if __name__== "__main__":
    a1=Voiture('Peugeot','bleue')
    a2=Voiture(couleur='verte')
    a3=Voiture('Mercedes')
    a1.Choix_conducteur('Khalil')
    a2.Choix_conducteur('Juliette')
    a2.accelerer(1.8,12)
    a2.accelerer(1.9,11)
    a1.afficher_tout()
    a2.afficher_tout()
    a3.afficher_tout()
    a1.accelerer(44,15)

    ## Affichage avec str
    print(str(a1))
    
    


        