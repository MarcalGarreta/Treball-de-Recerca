from tkinter import *

import math

root=Tk()

root.geometry("650x550")


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

frameLo=Frame(root)

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

frameLo.pack()

root.mainloop()