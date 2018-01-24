import glob
from bs4 import BeautifulSoup
import re
#import os

i = 0 

for fname in glob.iglob('**/*.html', recursive=True):
    if not fname.startswith("partials"):
        with open(fname) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            text = (soup.get_text())
            text = text.replace("\n", " ")
            regex = r"\{\{(.*?)\}\}"
            replacedText = re.sub(regex, '', text)
            finalText = re.sub("\s\s+" , " ", replacedText)
            print (finalText)
            htmlTextFile = open(fname + fname[0:5] + ".txt", "w")
#            os.remove(fname + fname[0:5] + ".txt")
            htmlTextFile.write(finalText)
            htmlTextFile.close()
            i += 1
            print(fname)