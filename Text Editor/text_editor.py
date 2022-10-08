import tkinter
import help
import error
from tkinter import filedialog

class TextEditor(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.CreateWidgets()
		self.initialize()

	def initialize(self):
		self.grid()

	def CreateWidgets(self):
		#This creates the widgets on the main frame and leads to the next frame.
		_ribbon=tkinter.Frame(self.parent, relief='raised', height='0.6c', width=320)
		_ribbon.grid_propagate(0)
		_ribbon.grid(row=0)

		_resetbutton=tkinter.Button(_ribbon, text='Reset', relief='flat', command=self.Reset)
		_resetbutton.grid()
		_helpbutton=tkinter.Button(_ribbon, text='Need help?', relief='flat', command=self.Help)
		_helpbutton.place(x='1.2c')

		_filelabel=tkinter.Label(self.parent, bg='light blue', text="Upload file")
		_filelabel.place(x='0.2c', y='0.7c')
		self.var1=tkinter.StringVar(self.parent)
		self.var1.set('C:/')
		self._filedirectory=tkinter.Entry(self.parent, width=38, textvariable=self.var1)
		self._filedirectory.grid_propagate(0)
		self._filedirectory.place(x='0.2c',y='1.2c')
		self._browsefile=tkinter.Button(self.parent, text='Browse File', command=self._browsefunc)
		self._browsefile.place(x='6.5c', y='1.1c')

		_filetypelabel=tkinter.Label(self.parent, bg='light blue', text='Target')
		_filetypelabel.place(x='0.2c', y='1.9c')
		self.var=tkinter.StringVar(self.parent)
		self.var.set("-Choose One-")
		_filetype=tkinter.OptionMenu(self.parent, self.var, "Characters", "Words")
		_filetype.config(bg='white', relief='flat')
		_filetype.place(x='0.2c', y='2.4c')

		_operationlabel=tkinter.Label(self.parent, bg='light blue', text="Choose operation")
		_operationlabel.place(x='0.2c', y='3.3c')
		self._operationtype=tkinter.Listbox(self.parent, height=2)
		self._operationtype.place(x='0.2c', y='3.8c')
		self._operationtype.insert(0,"Replace")
		self._operationtype.insert(1, "Delete")

		_nextbutton=tkinter.Button(self.parent, text="Next", command=self.Next)
		_nextbutton.place(x='4c', y='5c')

	def Next(self):
		#This handles the appropriate input parameters for the expected operation
		self._target=self.var.get()
		_filedirectory=self.var1.get()

		#First check for errors in input
		try:
			self._file=open(_filedirectory,'r')
		except FileNotFoundError:
			errors.Error(self,error.CheckFile)
			self._file.close()
			return
		if self._target=='-Choose One-':
			error.Error(self,error.NoTargType)
			self._file.close()
			return
		elif self._operationtype.curselection()==():
			error.Error(self,error.NoOperation)
			self._file.close()
			return
		else:
			#If no error was found, create a toplevel frame to get more input
			_newtop=tkinter.Toplevel(self.parent, bg='white')
			_newtop.grab_set()
			x=self.winfo_x()
			y=self.winfo_y()
			_newtop.geometry("200x90+{}+{}".format(45+x,60+y))
			if self._operationtype.curselection()[0]==0:
				_replacelabel=tkinter.Label(_newtop, bg='white', text="Replace:")
				_replacelabel.place(x='0.2c', y='0.2c')
				self._replaceword=tkinter.Entry(_newtop)
				self._replaceword.place(x='1.5c', y='0.2c')
				_withlabel=tkinter.Label(_newtop, bg='white', text="With:")
				_withlabel.place(x='0.2c', y='1c')
				self._withword=tkinter.Entry(_newtop)
				self._withword.place(x='1.5c', y='1c')
				_gobutton=tkinter.Button(_newtop, text="Go", command=self.Replace)
				_gobutton.place(x=95, y='1.6c')
			else:
				_deletelabel=tkinter.Label(_newtop, bg='white', text="Delete")
				_deletelabel.place(x='0.2c', y='0.5c')
				self._deleteword=tkinter.Entry(_newtop)
				self._deleteword.place(x='1.5c', y='0.5c')
				_gobutton=tkinter.Button(_newtop, text="Go", command=self.Delete)
				_gobutton.place(x=95, y='1.6c')
	def _browsefunc(self):
		filename=filedialog.askopenfilename()
		self.var1.set(filename)

	def Replace(self):
		oldword=self._replaceword.get().split(',')
		if len(oldword)>15:
			error.Error(self, error.TooLarge)
			self._file.close()
			return
		else:
			newword=self._withword.get().split(',')
			if len(oldword)!=len(newword):
				error.Error(self,error.LengthMismatch)
				self._file.close()
				return
			else:
				newfile=open(self.var1.get().split('.')[0]+'(Edited).'+self.var1.get().split('.')[1],'w')
				N=[0]*len(oldword)
				for line in self._file.readlines():
					for word in line.split(' '):
						if self._target=='Words':
							if word in oldword:
								i=oldword.index(word)
								newfile.write('%s ' % (newword[i]))
								N[i]+=1
							else:
								newfile.write('%s ' % (word))
						else:
							for char in word:
								if char in oldword:
									i=oldword.index(char)
									newfile.write('%s' % (newword[i]))
									N[i]+=1
								else:
									newfile.write('%s' % (char))
							newfile.write(' ')
					newfile.write('\n')
				self._file.close()
				newfile.close()
				error.Report(self,oldword,N,'replaced')

	def Delete(self):
		oldword=self._deleteword.get().split(', ')
		if len(oldword)>15:
			error.Error(self, error.TooLarge)
		else:
			newfile=open(self.var1.get().split('.')[0]+'(Edited).'+self.var1.get().split('.')[1],'w')
			N=[0]*len(oldword)
			for line in self._file.readlines():
				for word in line.split(' '):
					if self._target=='Words':
						if word in oldword:
							i=oldword.index(word)
							N[i]+=1
						else:
							newfile.write('%s ' % (word))
					else:
						for char in word:
							if char in oldword:
								i=oldword.index(char)
								N[i]+=1
							else:
								newfile.write('%s' % (char))
						newfile.write(' ')
				newfile.write('\n')
			self._file.close()
			newfile.close()
			error.Report(self,oldword,N,'deleted')

	def Reset(self):
		self._filedirectory.delete(0, len(self._filedirectory.get()))
		self._filename.delete(0, len(self._filename.get()))
		self._operationtype.selection_clear(self._operationtype.curselection())
		self.var.set("-Choose One-")

	def Help(self):
		help.Help(self,help.message)

if __name__=="__main__":
	app=TextEditor(None)
	app.configure(bg='light blue')
	app.title("Text Editor")
	win_height=220
	win_width=320
	screen_width=app.winfo_screenwidth()
	screen_height=app.winfo_screenheight()
	x=int((screen_width/2)-(win_width/2))
	y=int((screen_height/2)-(win_height/2))-30
	app.geometry("{}x{}+{}+{}".format(win_width, win_height, x,y))
	app.resizable(False, False)
	app.mainloop()
