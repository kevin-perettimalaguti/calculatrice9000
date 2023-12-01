# Importation de tkinter pour avoir une interface graphique
from tkinter import *

# Une classe qui contient toutes les fonctions pour calculer/afficher les chiffres/vérifier l'opération en cas d'erreur
class Calculator():
    def __init__(self): 
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0 
        self.entry = StringVar() 
        self.text = "" 
        self.signe = ""        
        
    def init(self):  
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0 
        self.text = "" 
        self.signe = ""
        
    def afficher_Nb(self): # Afficher les nombres sur l'écran 
        self.entry.set(self.text)
        ecran.delete("1.0", END)
        ecran.insert(END, self.text)

    def operation(self): # Vérification de l'opération
        try : 
            if "+" in self.text:
                self.Plus()
            elif "-" in self.text:
                self.Sous()
            elif "/" in self.text:
                self.Div()
            elif "x" in self.text:
                self.Mult()
        except:
            self.entry.set("ERROR")
            self.init()


    # Création des fonctions pour calculer: additionner, soustraire, mutiplier, diviser etc...    
    def Plus(self): # Addition
        nb = self.text.split("+")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 + self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Sous(self): # Soustraction
        nb = self.text.split("-")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 - self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Div(self): # Division
        nb = self.text.split("/")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 / self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Mult(self): # Multiplication
        nb = self.text.split("x")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 * self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Pourcentage(self):
        nb = float(self.text)
        resultat = nb / 100
        self.entry.set(str(resultat))
        self.init()    

# Fonctions pour activer tous les boutons
def Bouton1 (): 
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)    

def Bouton2 (): 
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)    

def Bouton3 (): 
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)    

def Bouton4 ():
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)    
    
def Bouton5 (): 
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)    

def Bouton6 ():
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)    

def Bouton7 (): 
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)    

def Bouton8 (): 
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def Bouton9 (): 
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text) 

def Bouton0 (): 
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)

def BoutonF(): 
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)    
    
def BoutonP (): 
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)    

def BoutonS (): 
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)    

def BoutonD ():
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)    

def BoutonM ():
    calculatrice.text += "x"
    calculatrice.entry.set(calculatrice.text)    

def BoutonE ():
    calculatrice.operation()    

def BoutonC (): 
    calculatrice.entry.set("")
    calculatrice.init()

def BoutonPourcentage():
    calculatrice.Pourcentage() 


# La fenêtre principale graphique
fenetre = Tk()
fenetre.title("Calculatrice programmable")
fenetre.geometry("360x450")

# Programme
calculatrice = Calculator()

# Ecran des calculs
ecran= Entry(fenetre, width=50, textvariable=calculatrice.entry, relief=SUNKEN, bd=5)
ecran.grid(columnspan=6, padx=20, pady=10)

# Parametrer les boutons de ma calculette
bouton1 = Button(fenetre, text="1", command=Bouton1, width=7, font=("Arial", 12), height=2) 
bouton2 = Button(fenetre, text="2", command=Bouton2, width=7, font=("Arial", 12), height=2) 
bouton3 = Button(fenetre, text="3", command=Bouton3, width=7, font=("Arial", 12), height=2)
bouton4 = Button(fenetre, text="4", command=Bouton4, width=7, font=("Arial", 12), height=2)
bouton5 = Button(fenetre, text="5", command=Bouton5, width=7, font=("Arial", 12), height=2) 
bouton6 = Button(fenetre, text="6", command=Bouton6, width=7, font=("Arial", 12), height=2)
bouton7 = Button(fenetre, text="7", command=Bouton7, width=7, font=("Arial", 12), height=2)
bouton8 = Button(fenetre, text="8", command=Bouton8, width=7, font=("Arial", 12), height=2)
bouton9 = Button(fenetre, text="9", command=Bouton9, width=7, font=("Arial", 12), height=2)
boutonC = Button(fenetre, text="C", command=BoutonC, width=7, font=("Arial", 12), height=2) 
bouton0 = Button(fenetre, text="0", command=Bouton0, width=7, font=("Arial", 12), height=2)
boutonPourcentage = Button(fenetre, text="%", command=BoutonPourcentage, width=7, font=("Arial", 12), height=2)
boutonParenthèseGauche = Button(fenetre, text="(", width=7, font=("Arial", 12), height=2)
boutonParenthèseDroite = Button(fenetre, text=")", width=7, font=("Arial", 12), height=2)
boutonPoint = Button(fenetre, text=".", command=BoutonF, width=7, font=("Arial", 12), height=2)
boutonPlus = Button(fenetre, text="+", command=BoutonP, width=7, font=("Arial", 12), height=2) 
boutonSous = Button(fenetre, text="-", command=BoutonS, width=7, font=("Arial", 12), height=2) 
boutonDiv = Button(fenetre, text="/", command=BoutonD, width=7, font=("Arial", 12), height=2) 
boutonMulti = Button(fenetre, text="x", command=BoutonM, width=7, font=("Arial", 12), height=2) 
boutonEgal = Button(fenetre, text="=", command=BoutonE, width=7, font=("Arial", 12), height=2)

# Organisation des boutons avec la fonction grid
bouton1.grid(row=1, column=1, padx=8, pady=8)
bouton2.grid(row=1, column=2, padx=8, pady=8)
bouton3.grid(row=1, column=3, padx=8, pady=8)
bouton4.grid(row=2, column=1, padx=8, pady=8)
bouton5.grid(row=2, column=2, padx=8, pady=8)
bouton6.grid(row=2, column=3, padx=8, pady=8)
bouton7.grid(row=3, column=1, padx=8, pady=8)
bouton8.grid(row=3, column=2, padx=8, pady=8)
bouton9.grid(row=3, column=3, padx=8, pady=8)
bouton0.grid(row=4, column=2, padx=8, pady=8)
boutonPoint.grid(row=4, column=3, padx=8, pady=8)
boutonPlus.grid(row=1, column=4, padx=8, pady=8)
boutonSous.grid(row=2, column=4, padx=8, pady=8)
boutonDiv.grid(row=3, column=4, padx=8, pady=8)
boutonMulti.grid(row=4, column=4, padx=8, pady=8)
boutonEgal.grid(row=5, column=4, padx=8, pady=8)
boutonC.grid(row=4, column=1, padx=8, pady=8)
boutonPourcentage.grid(row=5, column=3, padx=8, pady=8)
boutonParenthèseDroite.grid(row=5, column=2, padx=8, pady=8)
boutonParenthèseGauche.grid(row=5, column=1, padx=8, pady=8)

fenetre.mainloop() 
