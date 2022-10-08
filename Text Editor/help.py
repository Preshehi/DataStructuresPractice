import tkinter
from tkinter.font import Font

def Help(self, message):
	_helptoplevel=tkinter.Toplevel(self.parent)
	_helptoplevel.geometry('500x500')
	_helptoplevel.grab_set()
	_helptoplevel.title('Help')
	_helptoplevelin=tkinter.Frame(_helptoplevel, bg='white', height=460, width=480)
	_helptoplevelin.grid_propagate(0)
	_helptoplevelin.place(x=10, y=30)
	_helplabel=tkinter.Label(_helptoplevel, text='A little help never hurt anyone...')
	_helplabel.grid()
	_helpfont=Font(family='Arial', size=13)
	_helplabel.configure(font=_helpfont)
	_helpmessage=tkinter.Label(_helptoplevelin, justify='left', bg='white', text=message)
	_helpmessage.grid()
	_helpfont1=Font(family='Helvetica', size=11)
	_helpmessage.configure(font=_helpfont1)

message="""
This app is an easy to use app that helps to edit any of your text files,
ranging from .txt through .py up until .html files. However, there are
a few things to put at the back of your mind while using the app.


1) In order to increase the robustness, it is case sensitive so it is
pointless to put 'Point' when you mean 'point', either no result would
be produced or a wrong word would be deleted or replaced.

2) It can take multiple inputs. Hence, if this function is required,
words should be separated by a comma followed by a space (as is the
grammatical convention). Using another punctuation mark would yield
either an error or no action.
When using the replace function for multiple words, ensure the old word
and the word to replace it are at the same position in the sequence,
else, it would yield wrong results.

3) As a result of the unpredictability of the depth of nesting of folders
in your documents, you need to assist the app search for files by
providing the file directory using the appropriate convention which is:
'C:/Users/User/Desktop'
otherwise, an error pops.

PS: It does not overwrite the original file, so if you make a mistake,
fear not, you have a second chance.
"""
