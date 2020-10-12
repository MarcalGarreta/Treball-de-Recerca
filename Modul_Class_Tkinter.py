from tkinter import *

class Frame_:

	def __init__(self, root):

		self.root=root
		self.frame=Frame(self.root)

	def grid_(self, row_, column_, rowspan_, columnspan_):

		self.frame.grid(row=row_, column=column_, pady=10, padx=10, rowspan=rowspan_ , columnspan=columnspan_)

	def pack_(self):

		self.frame.pack()

class Label_:

	def __init__(self, frame, nom):

		self.frame=frame
		self.nom=nom
		self.label=Label(self.frame, text=self.nom)

	def grid_(self, row_, column_, rowspan_, columnspan_):

		self.label.grid(row=row_, column=column_, pady=10, padx=10, rowspan=rowspan_ , columnspan=columnspan_)

class Entry_:

	def __init__(self, frame, textvariable):

		self.frame=frame
		self.textvariable=textvariable
		self.entry=Entry(self.frame, textvariable=self.textvariable)
		self.entry.config(fg="red", justify="center")

	def grid_(self, row_, column_, rowspan_, columnspan_):

		self.entry.grid(row=row_, column=column_, pady=10, padx=10, rowspan=rowspan_ , columnspan=columnspan_)

class Button_:

	def __init__(self, frame, text, command):

		self.frame=frame
		self.text=text
		self.command=command
		self.button=Button(self.frame, text=self.text, command=self.command)

	def grid_(self, row_, column_, rowspan_, columnspan_):

		self.button.grid(row=row_, column=column_, pady=10, padx=10, rowspan=rowspan_ , columnspan=columnspan_)

class StringVar_:

	def __init__(self):

		self.stringVar=StringVar()

class Radiobutton_:

	def __init__(self, frame, text, variable, value, command):

		self.frame=frame
		self.text=text
		self.variable=variable
		self.value=value
		self.command=command
		self.radiobutton=Radiobutton(self.frame, text=self.text, variable=self.variable, value=self.value, command=self.command)

	def grid_(self, row_, column_, rowspan_, columnspan_):

		self.radiobutton.grid(row=row_, column=column_, pady=10, padx=10, rowspan=rowspan_ , columnspan=columnspan_)