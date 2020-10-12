from tkinter import *

import re

root=Tk()
root.geometry("300x300")

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

frameEq=Frame(root)

stringVarEq=StringVar()

labelTitolEq=Label(frameEq, text="Resolució d'equacions de primer grau:")
labelExplicacioEq=Label(frameEq)
entryEq=Entry(frameEq, textvariable=stringVarEq)
buttonCalculEq=Button(frameEq, text="Resoldre", command=lambda:equacions())

labelTitolEq.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
entryEq.grid(row=1, column=0, pady=10, padx=10)
buttonCalculEq.grid(row=1, column=1, pady=10, padx=10)

frameEq.pack()

root.mainloop()