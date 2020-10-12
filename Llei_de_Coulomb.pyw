from tkinter import *

import math

root=Tk()

root.geometry("850x550")


#---Calcul LLei de Coulomb---

resultatLc=0

resulatEntryLc=0

def calcLc():

	global resultatLc

	global resulatEntryLc

	try:

		if entryForcaLc.get()=="":

			entryForcaLc.config(fg="green")

			resultatLc=(round(float(stringConstantLc.get())*((float(stringCarrega1Lc.get())/1000000)*((float(stringCarrega2Lc.get())/1000000))/(float(stringDistanciaLc.get())**2)), 2))

			frameExplicacioForcaLc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)

			frameComprovantLc.grid(row=6, column=3, rowspan=2, pady=10, padx=10)

			resulatEntryLc=1

			print(resultatLc)

		elif entryConsantLc.get()=="":

			entryConsantLc.config(fg="green")

			resultatLc=(round((float(stringForcaLc.get()))*((float(stringDistanciaLc.get())**2))/((float(stringCarrega1Lc.get())/1000000)*((float(stringCarrega2Lc.get())/1000000))), 2))

			frameExplicacioConstantLc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)

			frameComprovantLc.grid(row=6, column=3, rowspan=2, pady=10, padx=10)

			resulatEntryLc=2

			print(resultatLc)

		elif entryCarrega1Lc.get()=="":

			entryCarrega1Lc.config(fg="green")

			resultatLc=(round(((float(stringForcaLc.get()))*((float(stringDistanciaLc.get())**2))/((float(stringCarrega2Lc.get())/1000000)*((float(stringConstantLc.get()))))*1000000), 2))

			frameExplicacioCarrega1Lc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)

			frameComprovantLc.grid(row=6, column=3, rowspan=2, pady=10, padx=10)

			resulatEntryLc=3

			print(resultatLc)

		elif entryCarrega2Lc.get()=="":

			entryCarrega2Lc.config(fg="green")

			resultatLc=(round(((float(stringForcaLc.get()))*((float(stringDistanciaLc.get())**2))/((float(stringCarrega1Lc.get())/1000000)*((float(stringConstantLc.get()))))*1000000), 2))

			frameExplicacioCarrega2Lc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)

			frameComprovantLc.grid(row=6, column=3, rowspan=2, pady=10, padx=10)
			
			resulatEntryLc=4

			print(resultatLc)

		elif entryDistanciaLc.get()=="":

			entryDistanciaLc.config(fg="green")

			resultatLc=(round(math.sqrt((((float(stringConstantLc.get()))*((float(stringCarrega1Lc.get())/1000000))*((float(stringCarrega2Lc.get())/1000000))))/((float(stringForcaLc.get())))), 2))

			frameExplicacioDistanciaLc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)
			
			frameComprovantLc.grid(row=6, column=3, rowspan=2, pady=10, padx=10)
			
			resulatEntryLc=5

			print(resultatLc)

	except ValueError:

		frameValueErrorLc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)

	except ZeroDivisionError:

		frameZeroDivisionErrorLc.grid(row=1, column=3, rowspan=5, pady=10, padx=10)


#---Netejar LLei de Coulomb---

def netejar(llistaString, llistaEntry):

	checkbuttonLc.deselect()
	
	for i in llistaString:

		i.set("")

	for i in llistaEntry:

		i.config(fg="red")

	for i in llistaFramesLc:

		i.grid_forget()



#---Funcio button seguent---

def comprovarLc():

	global resultatLc

	print(resultatLc)

	if resultatLc*0.99<float(stringComprovantLc.get())<resultatLc*1.01:

		if resulatEntryLc==1:
			stringForcaLc.set(resultatLc)

		elif resulatEntryLc==2:
			stringConstantLc.set(resultatLc)

		elif resulatEntryLc==3:
			stringCarrega1Lc.set(resultatLc)

		elif resulatEntryLc==4:
			stringCarrega2Lc.set(resultatLc)

		elif resulatEntryLc==5:
			stringDistanciaLc.set(resultatLc)

		"""for i in llistaFramesLc:

			i.grid_forget()"""

		#frameComprovantLc.grid_forget()

		labelCorrecteLc.grid(row=7, column=3, pady=10, padx=10)

	else:

		labelComprovantLc.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

		stringComprovantLc.set("")
		


#---CheckButton---

def checkbutton():

	if check.get()==1:

		stringConstantLc.set(9*(10**9))

	if check.get()==0:

		stringConstantLc.set("")



#---Fotos Llei de Coulomb---

imageForcaLc=PhotoImage(file="Formula_Llei_Coulomb_F.gif")

imageConstantLc=PhotoImage(file="Formula_Llei_Coulomb_K.gif")

imageCarrega1Lc=PhotoImage(file="Formula_Llei_Coulomb_Q.gif")

imageCarrega2Lc=PhotoImage(file="Formula_Llei_Coulomb_Q2.gif")

imageDistanciaLc=PhotoImage(file="Formula_Llei_Coulomb_r.gif")


#---Frames Explicaio---

frameLc=Frame(root)

frameExplicacioForcaLc=Frame(frameLc)
Label(frameExplicacioForcaLc, text="Per calcular la força en un problema sobre càrregues electriques es fa servir la llei de Coulomb:").grid(row=0, column=0, columnspan=2, pady=10, padx=10)
Label(frameExplicacioForcaLc, image=imageForcaLc).grid(row=1, column=0, columnspan=2, pady=10, padx=10)
Label(frameExplicacioForcaLc, text="Substitueix les incognites per les dades, calcula i Introdueix el resultat a la casella a sota").grid(row=2, column=0, columnspan=2, pady=10, padx=10)

frameExplicacioConstantLc=Frame(frameLc)
Label(frameExplicacioConstantLc, text="Per calcular la força en un problema sobre càrregues electriques es fa servir la llei de Coulomb:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioConstantLc, image=imageForcaLc).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioConstantLc, text="Com que has de calcular la constant elèctrica has d'aïllar la K. L'equació t'hauria de quedar així:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioConstantLc, image=imageConstantLc).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioConstantLc, text="Substitueix les incognites per les dades, calcula i Introdueix el resultat a la casella a sota").grid(row=4, column=0, pady=10, padx=10)

frameExplicacioCarrega1Lc=Frame(frameLc)
Label(frameExplicacioCarrega1Lc, text="Per calcular la força en un problema sobre càrregues electriques es fa servir la llei de Coulomb:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega1Lc, image=imageForcaLc).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega1Lc, text="Com que has de calcular la càrrega elèctrica 1 has d'aïllar la Q. L'equació t'hauria de quedar així:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega1Lc, image=imageCarrega1Lc).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega1Lc, text="Substitueix les incognites per les dades, calcula i Introdueix el resultat a la casella a sota").grid(row=4, column=0, pady=10, padx=10)

frameExplicacioCarrega2Lc=Frame(frameLc)
Label(frameExplicacioCarrega2Lc, text="Per calcular la força en un problema sobre càrregues electriques es fa servir la llei de Coulomb:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega2Lc, image=imageForcaLc).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega2Lc, text="Com que has de calcular la càrrega elèctrica 1 has d'aïllar la Q. L'equació t'hauria de quedar així:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega2Lc, image=imageCarrega2Lc).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioCarrega2Lc, text="Substitueix les incognites per les dades, calcula i Introdueix el resultat a la casella a sota").grid(row=4, column=0, pady=10, padx=10)

frameExplicacioDistanciaLc=Frame(frameLc)
Label(frameExplicacioDistanciaLc, text="Per calcular la força en un problema sobre càrregues electriques es fa servir la llei de Coulomb:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioDistanciaLc, image=imageForcaLc).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioDistanciaLc, text="Com que has de calcular la càrrega elèctrica 1 has d'aïllar la Q. L'equació t'hauria de quedar així:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioDistanciaLc, image=imageDistanciaLc).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioDistanciaLc, text="Substitueix les incognites per les dades, calcula i Introdueix el resultat a la casella a sota").grid(row=4, column=0, pady=10, padx=10)

frameValueErrorLc=Frame(frameLc)
Label(frameValueErrorLc, text="Introdueix numeros amb un punt actuant com a coma").grid(row=0, column=0, pady=10, padx=10)

frameZeroDivisionErrorLc=Frame(frameLc)
Label(frameZeroDivisionErrorLc, text="No es pot dividir per a zero").grid(row=0, column=0, pady=10, padx=10)

frameComprovantLc=Frame(frameLc)
stringComprovantLc=StringVar()
entryFrameComprovant=Entry(frameComprovantLc, textvariable=stringComprovantLc)
entryFrameComprovant.grid(row=0, column=0, pady=10, padx=10)
entryFrameComprovant.config(justify="center")
Button(frameComprovantLc, text="Següent", command=lambda:comprovarLc()).grid(row=0, column=1, pady=10, padx=10)
labelComprovantLc=Label(frameComprovantLc, text="Incorrecte, recorda seguir tots els passos")

labelCorrecteLc=Label(frameLc, text="Molt bé, el teu resultat es correcte")

llistaFramesExplicacioLc=[frameExplicacioForcaLc, frameExplicacioConstantLc, frameExplicacioCarrega1Lc, frameExplicacioCarrega2Lc, frameExplicacioDistanciaLc]

llistaFramesLc=[frameExplicacioForcaLc, frameExplicacioConstantLc, frameExplicacioCarrega1Lc, frameExplicacioCarrega2Lc, frameExplicacioDistanciaLc, frameValueErrorLc, frameZeroDivisionErrorLc]



#---Frame Llei de Coulomb---

labelTitol=Label(frameLc, text="Llei de Coulomb")
labelTitol.grid(row=0, column=0, pady=10, padx=10)
Label(frameLc, image=imageForcaLc).grid(row=0, column=1, pady=10, padx=10)

labelForcaLc=Label(frameLc, text="F, Força, N")
labelConsantLc=Label(frameLc, text="K, Constant elèctrica, N·m/C")
labelCarrega1Lc=Label(frameLc, text="Q, Càrrega elèctrica 1, µC")
labelCarrega2Lc=Label(frameLc, text="Q', Càrrega elèctrica 2, µC")
labelDistanciaLc=Label(frameLc, text="r, Distància, m")

llistaLabel=[labelForcaLc, labelConsantLc, labelCarrega1Lc, labelCarrega2Lc, labelDistanciaLc]

row=1

for i in llistaLabel:

	i.grid(row=row, column=0, pady=10, padx=10)

	row=row+1


stringForcaLc=StringVar()
stringConstantLc=StringVar()
stringCarrega1Lc=StringVar()
stringCarrega2Lc=StringVar()
stringDistanciaLc=StringVar()

llistaString=[stringForcaLc, stringConstantLc, stringCarrega1Lc, stringCarrega2Lc, stringDistanciaLc]

entryForcaLc=Entry(frameLc, textvariable=stringForcaLc)
entryConsantLc=Entry(frameLc, textvariable=stringConstantLc)
entryCarrega1Lc=Entry(frameLc, textvariable=stringCarrega1Lc)
entryCarrega2Lc=Entry(frameLc, textvariable=stringCarrega2Lc)
entryDistanciaLc=Entry(frameLc, textvariable=stringDistanciaLc)

llistaEntry=[entryForcaLc, entryConsantLc, entryCarrega1Lc, entryCarrega2Lc, entryDistanciaLc]

row=1

for i in llistaEntry:

	i.config(fg="red", justify="center")

	i.grid(row=row, column=1, pady=10, padx=10)

	row=row+1

check=IntVar()
checkbuttonLc=Checkbutton(frameLc, text="Buit", variable=check, onvalue=1, offvalue=0, command=checkbutton)
checkbuttonLc.grid(row=2, column=2, pady=10, padx=10)

'''for i in llistaVariables:

	label=Label(frameLc, text=i)

	label.grid(row=row, column=0, pady=10, padx=10)
	
	i=StringVar()

	entry=Entry(frameLc, textvariable=i)

	llistaString.append(i)

	entry.config(fg="red", justify="center")

	entry.grid(row=row, column=1, pady=10, padx=10)

	llistaEntry.append(entry)

	row=row+1'''

buttonCalcul=Button(frameLc, text="Calcular", command=lambda:calcLc())
buttonCalcul.grid(row=6, column=0, pady=10, padx=10)

buttonNetejar=Button(frameLc, text="Netejar", command=lambda:netejar(llistaString, llistaEntry))
buttonNetejar.grid(row=6, column=1, pady=10, padx=10)

Label(frameLc, justify=LEFT, text="F, Força: Força d'atracció o repulsió entre dues càrregues, Q i Q'. Newton, N\n"+
	"K, Constant elèctrica: Depen del medi, en l'aire o en el buit es igual a 9·10*9\n"+
	"Q, Carrega elèctrica 1: Microcoulomb, µC\n"+
	"Q', Carrega elèctrica 2: Microcoulomb, µC\n"+
	"r, Distància: Distància entre les càrregues Q i Q'. Metre, m").grid(row=7, column=0, columnspan=2, pady=10, padx=10)

frameLc.pack(side="left", anchor="n")


root.mainloop()