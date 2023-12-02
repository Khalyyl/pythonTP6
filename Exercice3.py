import math

class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def __str__(self):
        return f"Rayon: {self.rayon}"

    def affichage(self):
        print(self.rayon)

    def surface(self):
        return self.rayon * self.rayon * math.pi

class Cylindre(Cercle):

    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur = hauteur

    def volume(self):
        return self.hauteur * super().surface() 

class Cone(Cylindre):

    def __init__(self,rayon,hauteur):
        super().__init__(rayon,hauteur)

    def volume(self):
        return((Cylindre.volume(self)) / 3)
        

C1 = Cercle(6)
print(str(C1))
print("Surface:", C1.surface())

Cy = Cylindre(6, 2)
print("Volume:", Cy.volume())

Co = Cone(6,2)
print("Volume:", Co.volume())
