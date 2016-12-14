#!/usr/bin/python2.6
# -*-coding:Latin-1 -*

from Tkinter import *

#Fenetre principale
class Interface(Frame):

    

    def __init__(self, fenetre, **kwargs):

        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)

        self.pack(fill=BOTH)
		#Mise a zero variables vote
        self.nb_positif = 0
        self.nb_negatif = 0

        

        #Texte vote positif

        self.texte_positif = Label(self, text="Pas de votes positif.")

        self.texte_positif.pack()
        
        #Texte vote negatif
        self.texte_negatif = Label(self, text="Pas de votes negatifs")
        self.texte_negatif.pack()

        
		#Bouton quitter
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)

        self.bouton_quitter.pack(side="left")

        
		#Bouton vote positif
        self.bouton_positif = Button(self, text="Vote positif", fg="red",

                command=self.positif)

        self.bouton_positif.pack(side="right")
        
        #Bouton vote negatif
        self.bouton_negatif = Button(self, text="Vote Negatif", fg="red", command=self.negatif)
        self.bouton_negatif.pack(side="top")

    
	#Action bouton positif
    def positif(self):
        self.nb_positif += 1

        self.texte_positif["text"] = "{} Votes positifs.".format(self.nb_positif)
        
     #Action bouton negatif   
    def negatif(self):
        self.nb_negatif += 1

        self.texte_negatif["text"] = "{} Votes negatifs.".format(self.nb_negatif)


#Interface graphique
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy
