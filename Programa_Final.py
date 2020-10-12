from tkinter import *
import math
from Modul_Class_Tkinter import *
import re

root=Tk()
root.geometry("500x300")

menu=Menu(root)
root.config(menu=menu)

frameTotal=Frame(root)

def NetejarFrames():

	for i in llistaFramesTotals:

		i.pack_forget()

def LleiOhm():
	
	NetejarFrames()
	frameLo.pack()

def LleiCoulomb():

	NetejarFrames()
	frameLc.pack()

def MRUA():

	NetejarFrames()
	frameMRUA.frame.pack()

def EquacionsPrimerGrau():

	NetejarFrames()
	frameEq.pack()

problemaMenu=Menu(menu, tearoff=0)
problemaMenu.add_command(label="Calcular llei d'ohm", command=LleiOhm)
problemaMenu.add_command(label="Calcular llei de Coulomb", command=LleiCoulomb)
problemaMenu.add_command(label="Calcular MRUA", command=MRUA)
problemaMenu.add_command(label="Calcular equacions de primer grau", command=EquacionsPrimerGrau)

menu.add_cascade(label="Problema", menu=problemaMenu)



#------------------------Llei d'ohm-----------------------

#---Funcio Llei d'ohm---

def caclLleiOhm(entryResistencia, entryDiferenciaPotencial, entryIntensitat, stringvarResistencia, stringvarDiferenciaPotencial,
	 stringvarIntensitat, labelExplicacio, stringvarExplicacio, rowLabelExplicacio, columnaLabelExplicacio):
	
	if entryDiferenciaPotencial.get()=="":

		stringvarExplicacio.set(
			"Per calcular el valor de la diferència de potencial fem servir la llei d'Ohm:\n\n"+
			"I = V / R\n\n"+
			"Aïllem la R i obtenim que:\n\n"+
			"V = R · I\n\n"+
			"Substitueix els valors que tens i calcula")

		labelExplicacio.grid(row=rowLabelExplicacio, column=columnaLabelExplicacio, rowspan=7)

		diferenciaPotencialVariable=float(entryResistencia.get())*float(entryIntensitat.get())

		entryDiferenciaPotencialLo.config(fg="green")

		stringvarDiferenciaPotencial.set(round(diferenciaPotencialVariable, 2))

	elif entryIntensitat.get()=="":

		stringvarExplicacio.set("Per calcular el valor de la intenstitat fem servir la llei d'Ohm:\n\n"+
			"I = V / R\n\n"+
			"Substitueix els valors que tens i calcula")

		labelExplicacio.grid(row=rowLabelExplicacio, column=columnaLabelExplicacio, rowspan=7)

		intensitatVariable=float(entryDiferenciaPotencial.get())/float(entryResistencia.get())

		entryIntensitatLo.config(fg="green")

		stringvarIntensitat.set(round(intensitatVariable, 2))

	elif entryResistencia.get()=="":

		stringvarExplicacio.set("Per calcular el valor d'una resistència fem servir la llei d'Ohm:\n\n"+
			"I = V / R\n\n"+
			"Aïllem la R i obtenim que:\n\n"+
			"R = V / I\n\n"+
			"Substitueix els valors que tens i calcula")

		labelExplicacio.grid(row=rowLabelExplicacio, column=columnaLabelExplicacio, rowspan=7)

		resistenciaVariable=float(entryDiferenciaPotencial.get())/float(entryIntensitat.get())

		entryResistenciaLo.config(fg="green")

		stringvarResistencia.set(round(resistenciaVariable, 2))


def netejar(llistaString, llistEntry):

	for i in llistaString:

		i.set("")

	for i in llistaEntry:

		i.config(fg="red")

#--- Frame Llei d'ohm---

frameLo=Frame(frameTotal)

labelDadesLo=Label(frameLo, text="Dades:")
labelDadesLo.grid(row=0, column=0, pady=10, columnspan=2)

labelResistenciaLo=Label(frameLo, text="Resistència, ohm")
labelResistenciaLo.grid(row=1, column=0, pady=10)

labelDiferenciaPotencialLo=Label(frameLo, text="Diferencia de potencial, V")
labelDiferenciaPotencialLo.grid(row=2, column=0, pady=10)

labelIntensitatLo=Label(frameLo, text="Intensitat, A")
labelIntensitatLo.grid(row=3, column=0, pady=10)

explicacioLo=StringVar()
labelExplicacioLo=Label(frameLo, textvariable=explicacioLo, padx=10)

resistenciaLo=StringVar()
entryResistenciaLo=Entry(frameLo, textvariable=resistenciaLo)
entryResistenciaLo.config(fg="red", justify="center")
entryResistenciaLo.grid(row=1, column=1, pady=10)

diferenciaPotencialLo=StringVar()
entryDiferenciaPotencialLo=Entry(frameLo, textvariable=diferenciaPotencialLo)
entryDiferenciaPotencialLo.config(fg="red", justify="center")
entryDiferenciaPotencialLo.grid(row=2, column=1, pady=10)

intensitatLo=StringVar()
entryIntensitatLo=Entry(frameLo, textvariable=intensitatLo)
entryIntensitatLo.config(fg="red", justify="center")
entryIntensitatLo.grid(row=3, column=1, pady=10)

llistaStringvar=[resistenciaLo, diferenciaPotencialLo, intensitatLo]

llistaEntry=[entryResistenciaLo, entryDiferenciaPotencialLo, entryIntensitatLo]

buttoncalcLo=Button(frameLo, text="Calcular", command=lambda:caclLleiOhm(entryResistenciaLo, entryDiferenciaPotencialLo, entryIntensitatLo, 
	resistenciaLo, diferenciaPotencialLo, intensitatLo, labelExplicacioLo, explicacioLo, 1, 2))
buttoncalcLo.grid(row=4, column=0, pady=10)

buttonNetejarLo=Button(frameLo, text="Netejar", command=lambda:netejar(llistaStringvar, llistaEntry))
buttonNetejarLo.grid(row=4, column=1, pady=10)



#------------------------Llei de Coulomb-----------------------

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

		for i in llistaFramesLc:

			i.grid_forget()

		frameComprovantLc.grid_forget()

		labelCorrecteLc.grid(row=1, column=3, rowspan=6, pady=10, padx=10)

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

frameLc=Frame(frameTotal)

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

buttonCalcul=Button(frameLc, text="Calcular", command=lambda:calcLc())
buttonCalcul.grid(row=6, column=0, pady=10, padx=10)

buttonNetejar=Button(frameLc, text="Netejar", command=lambda:netejar(llistaString, llistaEntry))
buttonNetejar.grid(row=6, column=1, pady=10, padx=10)

Label(frameLc, justify=LEFT, text="F, Força: Força d'atracció o repulsió entre dues càrregues, Q i Q'. Newton, N\n"+
	"K, Constant elèctrica: Depen del medi, en l'aire o en el buit es igual a 9·10*9\n"+
	"Q, Carrega elèctrica 1: Microcoulomb, µC\n"+
	"Q', Carrega elèctrica 2: Microcoulomb, µC\n"+
	"r, Distància: Distància entre les càrregues Q i Q'. Metre, m").grid(row=7, column=0, columnspan=2, pady=10, padx=10)



#------------------------MRUA-----------------------

frameMRUA=Frame_(frameTotal)

#---Funcio Calcular---

def CalculMRUA():

	if radiobuttonVariableMRUA.get()==1:
		
		if textvariablePosicio.stringVar.get()!="" and textvariableVelocitatInicial.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryPosicioInicialMRUA.entry.config(fg="green")
				textvariablePosicioInicial.stringVar.set(round((float(textvariablePosicio.stringVar.get()))-(float(textvariableVelocitatInicial.stringVar.get())*float(textvariableTemps.stringVar.get()))-(0.5*float(textvariableAcceleracio.stringVar.get())*(float(textvariableTemps.stringVar.get())**2)),2))

			except ValueError:

				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else :

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)


	elif radiobuttonVariableMRUA.get()==2:

		if textvariablePosicioInicial.stringVar.get()!="" and textvariableVelocitatInicial.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryPosicioMRUA.entry.config(fg="green")
				textvariablePosicio.stringVar.set(round((float(textvariablePosicioInicial.stringVar.get()))+(float(textvariableVelocitatInicial.stringVar.get())*float(textvariableTemps.stringVar.get()))+(0.5*float(textvariableAcceleracio.stringVar.get())*(float(textvariableTemps.stringVar.get())**2)),2))

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else:

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)


	elif radiobuttonVariableMRUA.get()==3:
		
		if textvariableVelocitat.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryVelocitatInicialMRUA.entry.config(fg="green")
				textvariableVelocitatInicial.stringVar.set(round((float(textvariableVelocitat.stringVar.get()))-((float(textvariableAcceleracio.stringVar.get()))*(float(textvariableTemps.stringVar.get()))),2))
				frameExplicacioVelocitatInicialMRUA.grid(row=1, column=3, rowspan=6, pady=10, padx=10)

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else:

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)


	elif radiobuttonVariableMRUA.get()==4:
		
		if textvariableVelocitatInicial.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryVelocitatMRUA.entry.config(fg="green")
				textvariableVelocitat.stringVar.set(round((float(textvariableVelocitatInicial.stringVar.get()))+((float(textvariableAcceleracio.stringVar.get()))*(float(textvariableTemps.stringVar.get()))),2))
				frameExplicacioVelocitatMRUA.grid(row=1, column=3, rowspan=6, pady=10, padx=10)

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else:

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)


	elif radiobuttonVariableMRUA.get()==5:
		
		if textvariableVelocitatInicial.stringVar.get()!="" and textvariableVelocitat.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryAcceleracioMRUA.entry.config(fg="green")
				textvariableAcceleracio.stringVar.set(round(((float(textvariableVelocitat.stringVar.get()))-(float(textvariableVelocitatInicial.stringVar.get())))/(float(textvariableTemps.stringVar.get())),2))
				frameExplicacioAcceleracio_VelocitatMRUA.grid(row=1, column=3, rowspan=6, pady=10, padx=10)

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		elif textvariablePosicio.stringVar.get()!="" and textvariableVelocitatInicial.stringVar.get()!="" and textvariablePosicioInicial.stringVar.get()!="" and textvariableTemps.stringVar.get()!="":

			try:
				entryAcceleracioMRUA.entry.config(fg="green")
				textvariableAcceleracio.stringVar.set(round((float(textvariablePosicio.stringVar.get())-float(textvariablePosicioInicial.stringVar.get())-(float(textvariableVelocitatInicial.stringVar.get())*float(textvariableTemps.stringVar.get())))/(0.5*(float(textvariableTemps.stringVar.get())**2)),2))

			except ValueError:

				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else:

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)


	elif radiobuttonVariableMRUA.get()==6:
		
		if textvariableVelocitatInicial.stringVar.get()!="" and textvariableVelocitat.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="":

			try:
				entryTempsMRUA.entry.config(fg="green")
				textvariableTemps.stringVar.set(round(((float(textvariableVelocitat.stringVar.get()))-(float(textvariableVelocitatInicial.stringVar.get())))/(float(textvariableAcceleracio.stringVar.get())),2))
				frameExplicacioTemps_VelocitatMRUA.grid(row=1, column=3, rowspan=6, pady=10, padx=10)

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		elif textvariablePosicio.stringVar.get()!="" and textvariableVelocitatInicial.stringVar.get()!="" and textvariablePosicioInicial.stringVar.get()!="" and textvariableAcceleracio.stringVar.get()!="":

			try:
				a=0.5*float(textvariableAcceleracio.stringVar.get())
				b=float(textvariableVelocitatInicial.stringVar.get())
				c=float(textvariablePosicioInicial.stringVar.get())-float(textvariablePosicio.stringVar.get())

				entryTempsMRUA.entry.config(fg="green")
				textvariableTemps.stringVar.set(round((-b+(math.sqrt(b**2-4*a*c)))/(2*a),2))

			except ValueError:
				frameValorIncorrecteMRUA.grid_(1, 4, 6, 1)

		else:

			frameIncorrecteMRUA.grid_(1, 4, 6, 1)




#---Funcio Radiobutton---

def Radiobuttonn():

	if radiobuttonVariableMRUA.get()==1:
		buttonCalculMRUA.button.config(text="Calcular x0")
	
	elif radiobuttonVariableMRUA.get()==2:
		buttonCalculMRUA.button.config(text="Calcular x")

	elif radiobuttonVariableMRUA.get()==3:
		buttonCalculMRUA.button.config(text="Calcular v0")

	elif radiobuttonVariableMRUA.get()==4:
		buttonCalculMRUA.button.config(text="Calcular v")

	elif radiobuttonVariableMRUA.get()==5:
		buttonCalculMRUA.button.config(text="Calcular a")

	elif radiobuttonVariableMRUA.get()==6:
		buttonCalculMRUA.button.config(text="Calcular t")

#---Funcio Netejar---

def NetejarMRUA():

	for i in llistaTextvariable:

		i.set("")

	for i in llistaEntryMRUA:

		i.config(fg="red")

	for i in llistaFrameExplicacio:

		i.grid_forget()


#---Label---

labelDadesMRUA=Label_(frameMRUA.frame, "Dades:")
labelDadesMRUA.grid_(0, 0, 1, 2)

labelPosicioInicialMRUA=Label_(frameMRUA.frame, "Posició inicial, x0")
labelPosicioInicialMRUA.grid_(1, 0, 1, 1)

labelPosicioMRUA=Label_(frameMRUA.frame, "Posició final, x")
labelPosicioMRUA.grid_(2, 0, 1, 1)

labelVelocitatInicialMRUA=Label_(frameMRUA.frame, "Velocitat inicial, v0")
labelVelocitatInicialMRUA.grid_(3, 0, 1, 1)

labelVelocitatMRUA=Label_(frameMRUA.frame, "Velocitat final, v")
labelVelocitatMRUA.grid_(4, 0, 1, 1)

labelAcceleracioMRUA=Label_(frameMRUA.frame, "Acceleració, a")
labelAcceleracioMRUA.grid_(5, 0, 1, 1)

labelTempsMRUA=Label_(frameMRUA.frame, "Temps, t")
labelTempsMRUA.grid_(6, 0, 1, 1)



#---StringVar---

textvariablePosicioInicial=StringVar_()
textvariablePosicio=StringVar_()
textvariableVelocitatInicial=StringVar_()
textvariableVelocitat=StringVar_()
textvariableAcceleracio=StringVar_()
textvariableTemps=StringVar_()

llistaTextvariable=[textvariablePosicioInicial.stringVar, textvariablePosicio.stringVar, textvariableVelocitatInicial.stringVar,
	textvariableVelocitat.stringVar, textvariableAcceleracio.stringVar, textvariableTemps.stringVar]



#---Entry---

entryPosicioInicialMRUA=Entry_(frameMRUA.frame, textvariablePosicioInicial.stringVar)
entryPosicioInicialMRUA.grid_(1, 1, 1, 1)

entryPosicioMRUA=Entry_(frameMRUA.frame, textvariablePosicio.stringVar)
entryPosicioMRUA.grid_(2, 1, 1, 1)

entryVelocitatInicialMRUA=Entry_(frameMRUA.frame, textvariableVelocitatInicial.stringVar)
entryVelocitatInicialMRUA.grid_(3, 1, 1, 1)

entryVelocitatMRUA=Entry_(frameMRUA.frame, textvariableVelocitat.stringVar)
entryVelocitatMRUA.grid_(4, 1, 1, 1)

entryAcceleracioMRUA=Entry_(frameMRUA.frame, textvariableAcceleracio.stringVar)
entryAcceleracioMRUA.grid_(5, 1, 1, 1)

entryTempsMRUA=Entry_(frameMRUA.frame, textvariableTemps.stringVar)
entryTempsMRUA.grid_(6, 1, 1, 1)

llistaEntryMRUA=[entryPosicioInicialMRUA.entry, entryPosicioMRUA.entry, entryVelocitatInicialMRUA.entry, entryVelocitatMRUA.entry,
	entryAcceleracioMRUA.entry, entryTempsMRUA.entry]

#---Radiobutton---

radiobuttonVariableMRUA=IntVar()

radiobuttonPosicioInicialMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 1, lambda:Radiobuttonn())
radiobuttonPosicioInicialMRUA.grid_(1, 2, 1, 1)

radiobuttonPosicioMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 2, lambda:Radiobuttonn())
radiobuttonPosicioMRUA.grid_(2, 2, 1, 1)

radiobuttonVelocitatInicialMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 3, lambda:Radiobuttonn())
radiobuttonVelocitatInicialMRUA.grid_(3, 2, 1, 1)

radiobuttonVelocitatMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 4, lambda:Radiobuttonn())
radiobuttonVelocitatMRUA.grid_(4, 2, 1, 1)

radiobuttonAcceleracioMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 5, lambda:Radiobuttonn())
radiobuttonAcceleracioMRUA.grid_(5, 2, 1, 1)

radiobuttonTempsMRUA=Radiobutton_(frameMRUA.frame, "", radiobuttonVariableMRUA, 6, lambda:Radiobuttonn())
radiobuttonTempsMRUA.grid_(6, 2, 1, 1)



#---Imatges---

imageVelocitatMRUA=PhotoImage(file="Formula_MRUA_Velocitat.gif")
imageVelocitatInicialMRUA=PhotoImage(file="Formula_MRUA_Velocitat_Inicial.gif")
imageAcceleracio_VelocitatMRUA=PhotoImage(file="Formula_MRUA_Acceleracio-Velocitat.gif")
imageTemps_VelocitatMRUA=PhotoImage(file="Formula_MRUA_Temps-Velocitat.gif")

#---Frames  Explicació---

frameExplicacioVelocitatMRUA=Frame(frameMRUA.frame)
Label(frameExplicacioVelocitatMRUA, text="Per calcular la velocitat en un problema sobre el MRUA es fa servir la següent fórmula:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatMRUA, image=imageVelocitatMRUA).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatMRUA, text="Substitueix les incògnites per les dades i calcula.").grid(row=2, column=0, pady=10, padx=10)

frameExplicacioVelocitatInicialMRUA=Frame(frameMRUA.frame)
Label(frameExplicacioVelocitatInicialMRUA, text="Per calcular la velocitat inicial en un problema sobre el MRUA es fa servir la següent fórmula:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatInicialMRUA, image=imageVelocitatMRUA).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatInicialMRUA, text="Ara aïlla la velocitat inicial en la fórmula:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatInicialMRUA, image=imageVelocitatInicialMRUA).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioVelocitatInicialMRUA, text="Substitueix les incògnites per les dades i calcula.").grid(row=4, column=0, pady=10, padx=10)

frameExplicacioAcceleracio_VelocitatMRUA=Frame(frameMRUA.frame)
Label(frameExplicacioAcceleracio_VelocitatMRUA, text="Per calcular l'acceleració en un problema sobre el MRUA es fa servir la següent fórmula:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioAcceleracio_VelocitatMRUA, image=imageVelocitatMRUA).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioAcceleracio_VelocitatMRUA, text="Ara aïlla l'acceleració en la fórmula:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioAcceleracio_VelocitatMRUA, image=imageAcceleracio_VelocitatMRUA).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioAcceleracio_VelocitatMRUA, text="Substitueix les incògnites per les dades i calcula.").grid(row=4, column=0, pady=10, padx=10)

frameExplicacioTemps_VelocitatMRUA=Frame(frameMRUA.frame)
Label(frameExplicacioTemps_VelocitatMRUA, text="Per calcular el temps en un problema sobre el MRUA es fa servir la següent fórmula:").grid(row=0, column=0, pady=10, padx=10)
Label(frameExplicacioTemps_VelocitatMRUA, image=imageVelocitatMRUA).grid(row=1, column=0, pady=10, padx=10)
Label(frameExplicacioTemps_VelocitatMRUA, text="Ara aïlla el temps en la fórmula:").grid(row=2, column=0, pady=10, padx=10)
Label(frameExplicacioTemps_VelocitatMRUA, image=imageTemps_VelocitatMRUA).grid(row=3, column=0, pady=10, padx=10)
Label(frameExplicacioTemps_VelocitatMRUA, text="Substitueix les incògnites per les dades i calcula.").grid(row=4, column=0, pady=10, padx=10)


frameIncorrecteMRUA=Frame_(frameMRUA.frame)

labelIncorrecteMRUA=Label_(frameIncorrecteMRUA.frame, "Dades insuficients")
labelIncorrecteMRUA.grid_(0, 0, 1, 1)

frameValorIncorrecteMRUA=Frame_(frameMRUA.frame)

labelValorIncorrecteMRUA=Label_(frameValorIncorrecteMRUA.frame, "Valors incorrectes, només es poden introduir números")
labelValorIncorrecteMRUA.grid_(0, 0, 1, 1)

llistaFrameExplicacio=[frameIncorrecteMRUA.frame, frameValorIncorrecteMRUA.frame, frameExplicacioVelocitatMRUA]


#---Button---

buttonCalculMRUA=Button_(frameMRUA.frame, "Calcular", lambda:CalculMRUA())
buttonCalculMRUA.grid_(7, 0, 1, 1)

buttonNetejarMRUA=Button_(frameMRUA.frame, "Netejar", lambda:NetejarMRUA())
buttonNetejarMRUA.grid_(7, 1, 1, 1)



#------------------------Equacions Primer Grau-----------------------

#---Funcio Grau1---

def equacions():

	equacioEsquerraIgual=re.sub("=.*$", "", entryEq.get())
	llistaXEsquerraIgual=re.findall("[\+\-][0-9]*x", equacioEsquerraIgual)

	totalXEsquerraIgual=""

	for i in llistaXEsquerraIgual:

		totalXEsquerraIgual=totalXEsquerraIgual+i

	equacioDretaIgual=re.sub("^.*=", "", entryEq.get())
	llistaXDretaIgual=re.findall("[\+\-][0-9]*x", equacioDretaIgual)

	totalXDretaIgual=""

	for i in llistaXDretaIgual:

		if re.search("\+", i) is not None:
			totalXDretaIgual=totalXDretaIgual+re.sub("\+", "-", i)

		else:
			totalXDretaIgual=totalXDretaIgual+re.sub("\-", "+", i)

	totalX=totalXEsquerraIgual+totalXDretaIgual
	print(totalX)


	equacioEsquerraIgualTermesI=re.sub("[\+\-][0-9]*x", "", equacioEsquerraIgual)
	resolucioEsquerraIgualTermesI=re.findall("[\+\-][0-9]*", equacioEsquerraIgualTermesI)

	totalTermesIEsquerraIgual=""

	for i in resolucioEsquerraIgualTermesI:
		
		if re.search("\+", i) is not None:
			totalTermesIEsquerraIgual=totalTermesIEsquerraIgual+re.sub("\+", "-", i)

		else:
			totalTermesIEsquerraIgual=totalTermesIEsquerraIgual+re.sub("\-", "+", i)

	equacioDretaIgualTermesI=re.sub("[\+\-][0-9]*x", "", equacioDretaIgual)
	resolucioDretaIgualTermesI=re.findall("[\+\-][0-9]*", equacioDretaIgualTermesI)

	totalTermesIDretaIgual=""

	for i in resolucioDretaIgualTermesI:
		
		totalTermesIDretaIgual=totalTermesIDretaIgual+i

	totalTermesI=totalTermesIDretaIgual+totalTermesIEsquerraIgual
	print(totalTermesI)

	equacioFinal=totalX+"="+totalTermesI
	print(equacioFinal)


	equacioResultatX=re.findall("[\+\-][0-9]*", totalX)
	resultatX=0

	for i in equacioResultatX:

		resultatX+=int(re.findall("[\+\-][0-9]*", i)[0])

	equacioResultatTermesI=re.findall("[\+\-][0-9]*", totalTermesI)
	resultatTermesI=0

	for i in equacioResultatTermesI:

		resultatTermesI+=int(re.findall("[\+\-][0-9]*", i)[0])

	equacioResultatTotal=str(resultatX)+"x="+str(resultatTermesI)
	print(equacioResultatTotal)

	equacioResultatFinal="x="+str(resultatTermesI)+"/"+str(resultatX)
	print(equacioResultatFinal)

	resultatFinal="x="+str(resultatTermesI/resultatX)
	print(resultatFinal)


	text="Primer posem les x en un costat i els números en l'altre canviant el signe quan canviem de costat\n\n"+equacioFinal+"\n\n"+"Seguidament calculem el total de cada costat\n\n"+equacioResultatTotal+"\n\n"+"Ara pasem el número que esta multiplicant la x a l'altre costat dividint\n\n"+equacioResultatFinal+"\n\nSeguidament calculem el resultat final\n\n"+resultatFinal


	labelExplicacioEq.config(text=text)

	labelExplicacioEq.grid(row=2, column=0, pady=10, padx=10, columnspan=2)


#---Intericie---

frameEq=Frame(frameTotal)

stringVarEq=StringVar()

labelTitolEq=Label(frameEq, text="Resolució d'equacions de primer grau:")
labelExplicacioEq=Label(frameEq)
entryEq=Entry(frameEq, textvariable=stringVarEq)
buttonCalculEq=Button(frameEq, text="Resoldre", command=lambda:equacions())

labelTitolEq.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
entryEq.grid(row=1, column=0, pady=10, padx=10)
buttonCalculEq.grid(row=1, column=1, pady=10, padx=10)





llistaFramesTotals=[frameLc, frameLo, frameMRUA.frame, frameEq]

frameTotal.pack(side="left", anchor="n")
root.mainloop()