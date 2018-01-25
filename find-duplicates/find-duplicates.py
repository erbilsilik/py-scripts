wordList = """"Kit Salido"
"Kit Salido"
"Verlie Szabo"
"Verlie Szabo"
"Laurene Edington"
"Darwin Chamberlain"
"Augusta Grossi"
"Augusta Grossi"
"Patti Westray"
"James Stoecker"
"Genny Palacio"
"Shakita Sabia"
"Ofelia Danielsen"
"Ofelia Danielsen"
"Ofelia Danielsen"
"Ofelia Danielsen"
"Sherlyn Swager"
"Natasha Screen"
"Alayna Dermody"
"Daphne Beale"
"Daphne Beale"
"Daphne Beale"
"Cristy Cai"
"Angelic Cazarez"
"Angelic Cazarez"
"Kasey Belville"
"Scarlet Allmond"
"Scarlet Allmond"
"Hollis Boden"
"Angeline Cochran"
"""

wordsArray = wordList.split("\n") 

words = {}
duplicates = open("duplicates.txt", "w")
total = 0

for word in wordsArray:
  try:
    words[word] += 1
  except:
    words[word] = 1

for k, v in words.items():
    if v > 1:
        print("{0} : {1}".format(k, v))
        excess = v - 1
        total += excess
        duplicates.write("{0} : {1}\n".format(k, v))
print ("------------------------------------")
print ("Total Duplicates: {}".format(total))
print ("------------------------------------")
duplicates.write("------------------------------------")
duplicates.write("\nTotal Duplicates: {}\n".format(total))
duplicates.write("------------------------------------")
duplicates.close()