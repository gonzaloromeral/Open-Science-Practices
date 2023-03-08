from grobid_client.grobid_client import GrobidClient
import tkinter
from tkinter import filedialog
import os
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

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
list1 = []
i = 1
contenido = os.listdir(file_path_variable)
xml = []
for fichero in contenido:
    aux = os.path.normpath(os.path.join(file_path_variable , fichero))
    print(aux)
    if os.path.isfile(aux) and fichero.endswith('.xml'):
        xml.append(aux)


for unit in xml:
    list1.append("Archivo" + str(i))
    i = i + 1
    content = []
    with open(unit, "r", encoding="utf8") as file:
        content = file.readlines()
    content1 = "".join(content)
    bs_content = bs(content1, "lxml")
    result1 = bs_content.find_all("term")
    for each in result1:
        listaglobalKeywords.append(each.get_text())
    result2 = bs_content.find_all("figure")
    listaglobalnFiguras.append(len(result2))
    result3 = bs_content.find_all("ptr")
    list2 = []
    for each in bs_content.find_all("ptr"):
        list2.append(each.get("target"))
    listagloballinks.append(list2)

word_cloud_dict = Counter(listaglobalKeywords)
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_cloud_dict)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig(os.path.join(file_path_variable, "wordcloud.png"))
plt.clf()
x2 = plt.bar(list1, listaglobalnFiguras)
plt.savefig(os.path.join(file_path_variable, "figuras.png"))
with open(os.path.join(file_path_variable, "links.txt"), 'w') as temp_file:
    for item in listagloballinks:
        temp_file.write("%s\n" % item)
