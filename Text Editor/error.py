import tkinter
from tkinter.font import Font

class Error(Exception):
	pass

def Error(self,message):
	_errortoplevel=tkinter.Toplevel(self.parent, bg='white')
	_errortoplevel.grab_set()
	x=self.winfo_x()
	y=self.winfo_y()
	_errortoplevel.geometry('300x100+{}+{}'.format(70+x,55+y))
	_errortoplevel.title('Error!')
	_errorfont=Font(family='lucinda', size=10)
	_errorlabel=tkinter.Label(_errortoplevel, bg='white', text=message, wraplength=280)
	_errorlabel.grid()
	_errorlabel.config(font=_errorfont)

def Report(self, D, N, oper):
	_reporttoplevel=tkinter.Toplevel(self.parent)
	_reporttoplevel.grab_set()
	n=len(D)
	_reportlabel=tkinter.Label(_reporttoplevel, text='Done!\nWord(s) '+oper+' is/are:')
	_reportlabel.grid(sticky='W', row=0, column=0)
	text=''
	for i in range(n):
		text=text+D[i]+': '+str(N[i])+'\n'
	_result=tkinter.Label(_reporttoplevel, text=text)
	_result.grid(row=1, column=0, sticky='W')
	x=230
	y=40+(20*n)
	x1=self.winfo_screenwidth()
	y1=self.winfo_screenheight()
	x2=int((x1-x)/2)
	y2=int(((y1-y)/2)-30)
	_reporttoplevel.geometry("{}x{}+{}+{}".format(x,y,x2,y2))
	_reporttoplevel.title("Report")

CheckFile="""
Alas, I findeth not that which you seek. Fret not, check that thou proclaimeth a valid directory or file name.
"""

TooLarge="""
Ye might have bitten what thoudst can not chew. Words must not be more than 15.
"""

NoOperation="""
Let it be said across seas and oceans, that no man shalt get any operation done without knowing the type.
"""

NoTargType="""
Thou art failed to proclaim the target, how can I shoot?
"""

LengthMismatch="""
Amount of words to be replaced and that of their replacement must be equal.
"""
