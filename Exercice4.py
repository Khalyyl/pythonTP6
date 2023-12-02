import datetime

class NB_jours:
    nb_jours = (31,28,31,30,31,30,31,31,30,31,30,31)

class Date(NB_jours):

    def __init__(self,jour,mois,année):
        self.jour=jour
        self.mois=mois
        self.année=année
    
    def affiche_date(self):
        print(f"{self.jour} - {self.mois} - {self.année}")
    
class Adresse:

    def __init__(self,num,rue,ville):
        if isinstance(num ,str) and num.isdigit() and len(num)== 2:
            self.__num=num
        else:
            raise ValueError("L'attribut 'num' doit être une chaîne de 2 chiffres.")

        self.__rue=rue
        self.__ville=ville
    
class Personne:

    def __init__(self,nom,adresse,date_naissance):
        self.nom=nom
        self.adresse=adresse
        self.date_naissance=date_naissance
        self.__age=self.calculDate()

    def calculDate(self):
        aujourd_hui = Date(2, 12, 2023)
        age = aujourd_hui.année - self.date_naissance.année - ((aujourd_hui.mois, aujourd_hui.jour) < (self.date_naissance.mois, self.date_naissance.jour))
        return age

    def affiche_personne(self):
        print(f"Nom :{self.nom} -- adresse : {self.adresse} -- {self.date_naissance} --  age :{self.__age} ans " )

if __name__=="__main__": 

    date_x=Date(6,7,2000)
    adresse_x = Adresse('07','ali belhouane','Sousse')  
    personne_x = Personne('Foulen',adresse_x,date_x)
    print(personne_x.affiche_personne())





    