from tkinter import *

from Modul_Class_Tkinter import *

import math

root=Tk()
root.geometry("600x400")

frameMRUA=Frame_(root)



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




frameMRUA.pack_()

root.mainloop()