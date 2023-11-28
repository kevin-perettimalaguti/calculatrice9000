from tkinter import *

fenetre = Tk()
fenetre.title("Calculatrice programmable")
fenetre.geometry("410x500")

# Écran principal
ecran = Text(fenetre, width=20, height=2, font=("Arial", 26))
ecran.grid(columnspan=5, padx=10, pady=10)

# Fonctions des boutons de la calculatrice (hors opérateur)
class Boutons:
    def __init__(self, valeur, row, column):
        self.bouton = Button(fenetre, text=valeur, command=lambda: self.ajout_valeur(valeur), width=8, font=("Arial", 13), height=2)
        self.bouton.grid(row=row, column=column, padx=6, pady=6)

    def ajout_valeur(self, valeur):
        afficher = ecran.get("1.0", END)
        ecran.delete("1.0", END)
        ecran.insert(END, afficher.strip() + valeur)

# Instanciation des boutons (chiffres)
bouton1 = Boutons("1", 1, 1)
bouton2 = Boutons("2", 1, 2)
bouton3 = Boutons("3", 1, 3)
bouton4 = Boutons("4", 2, 1)
bouton5 = Boutons("5", 2, 2)
bouton6 = Boutons("6", 2, 3)
bouton7 = Boutons("7", 3, 1)
bouton8 = Boutons("8", 3, 2)
bouton9 = Boutons("9", 3, 3)
bouton0 = Boutons("0", 4, 2)

# Opérations
class Operations:
    def __init__(self, symbole, row, column):
        self.operation = Button(fenetre, text=symbole, command=lambda: self.operation_clique(symbole), width=8, font=("Arial", 13), height=2)
        self.operation.grid(row=row, column=column, padx=6, pady=6)

    def operation_clique(self, symbole):
        current = ecran.get("1.0", END)
        if current and current[-1] not in ['+', '-', 'x', '/']:
            ecran.insert(END, symbole) 

# Fonction du bouton effacer
def effacer_tout():        
    ecran.delete("1.0", END)

# Instanciation des boutons opérateurs
operation_plus = Operations("+", 1, 4)
operation_moins = Operations("-", 2, 4)
operation_fois = Operations("x", 3, 4)
operation_div = Operations("/", 4, 4)

# Boutons égal, effacer, virgule, parenthèses
pourcentage = Boutons("%", 4, 3)
egal = Boutons("=", 5, 4)
effacer = Button(fenetre, text="C", command=effacer_tout, width=8, font=("Arial", 13), height=2)
effacer.grid(row=4, column=1, padx=6, pady=6)
virgule = Boutons(".", 5, 2)
parenthese_gauche = Boutons("(", 5, 1 )
parenthese_droite = Boutons(")", 5, 3)

fenetre.mainloop()
