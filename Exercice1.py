## PARTIE 1/

class Rectangle:

    def __init__(self, longueur=1, largeur=1):
        self.nom = 'rectangle'
        self.longueur = longueur
        self.largeur = largeur

    def affichage(self):
        print(f"{self.nom} - Longueur: {self.longueur}, Largeur: {self.largeur}")

    def surface(self):
        return self.longueur * self.largeur

class Carre(Rectangle):
    
    def __init__(self, cote=1):
        super().__init__(cote, cote)  # Appel du constructeur de la classe parente
        self.nom = 'carré'


## PARTIE 2/

class Point():
    
    def __init__(self, x=0.0,y=0.0):
        self.x=x
        self.y=y
    
    def __str__(self) :
        return(f"Point({self.x}, {self.y})")
    
    def affichage():
        print(f"Point({self.x},{self.y})")

class Segment(Point):

    def __init__(self,x1,y1,x2,y2):
        self.orig=Point(x1,y1)
        self.exterem=Point(x2,y2)

    def __str__(self):
        return(f"Origine :{self.orig} , Extremité : {self.exterem}")
    
    def afficher(self):
        print("Origine")
        self.orig.affichage()
        print("Extremité")
        self.exterem.afficher()



# Exemple d'utilisation
rectangle = Rectangle()
rectangle_custom = Rectangle(4, 6)
## Carre par default ( en utilisant les parametres de constructeur par default )
carre = Carre()
## carre avec insertion de parametre :
carre_custom = Carre(5)

# Affichage des informations

rectangle.affichage()
print("Surface:", rectangle.surface())
print()

rectangle_custom.affichage()
print("Surface:", rectangle_custom.surface())
print()

carre.affichage()
print("Surface:", carre.surface())
print()

carre_custom.affichage()
print("Surface:", carre_custom.surface())
print()

carre_custom = Carre(3)
carre_custom.affichage()
print("Surface:", carre_custom.surface())

print()
Rectangle1 = Rectangle(3,9)
Rectangle1.affichage()
print("Surface de Rectangle :",Rectangle1.surface())

segment1 = Segment(1, 2, 3, 4)
print(str(segment1))