from bs4 import BeautifulSoup
from glob import glob
import re

for fname in glob("*.html"):
    with open(fname) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        text = (soup.get_text())
        text = text.replace("\n", " ")
        regex = r"\{\{(.*?)\}\}"
        replacedText = re.sub(regex, '', text)
        finalText = re.sub("\s\s+" , " ", replacedText)
        print (finalText)
        htmlTextFile = open(fname[0:5] + ".txt", "w")
        htmlTextFile.write(finalText)
        htmlTextFile.close()