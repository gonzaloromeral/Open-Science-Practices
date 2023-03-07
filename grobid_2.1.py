from grobid_client.grobid_client import GrobidClient
import tkinter
from tkinter import filedialog
import os
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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

listaglobalKeywords = []
listaglobalnFiguras = []
listagloballinks = []

contenido = os.listdir(file_path_variable)
xml = []
for fichero in contenido:
    aux = os.path.normpath(os.path.join(file_path_variable , fichero))
    print(aux)
    if os.path.isfile(aux) and fichero.endswith('.xml'):
        xml.append(aux)

print(xml)

for unit in xml:

    content = []
    with open(unit, "r", encoding="utf8") as file:
        content = file.readlines()

    content1 = "".join(content)
    bs_content = bs(content1, "lxml")
    result1 = bs_content.find_all("term")
    list1 = []
    for each in result1:
        list1.append(each.get_text())

    listaglobalKeywords.append(list1)
    result2 = bs_content.find_all("figure")
    listaglobalnFiguras.append(len(result2))
    result3 = bs_content.find_all("ptr")
    list2 = []
    for each in bs_content.find_all("ptr"):
        list2.append(each.get("target"))

    listagloballinks.append(list2)

unique_string=(" ").join(listaglobalKeywords)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')

plt.bar(listaglobalnFiguras)
print(listagloballinks)
plt.show()
