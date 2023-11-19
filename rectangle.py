class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur 
        self.largeur = largeur 
    def perimetre(self):
        self.perimetre = 2*(self.longueur + self.largeur)
        return self.perimetre
    def Aire(self):
        self.Aire = self.longueur * self.largeur
        return self.Aire
    def isCrre(self):
        if self.longueur == self.largeur :
            return "vrai"
        else :
            return "faux"
    def afficherRectangle(self):
        print(self.largeur,self.longueur,self.perimetre,self.Aire,self.isCrre)

