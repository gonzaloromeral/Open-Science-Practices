from grobid_client.grobid_client import GrobidClient
import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You choose: %s" % tempdir)
    return tempdir


file_path_variable = search_for_file_path()
print ("\nfile_path_variable = ", file_path_variable)

client = GrobidClient()
client.process("processFulltextDocument", file_path_variable)

