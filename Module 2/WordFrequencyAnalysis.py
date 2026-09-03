allText = {} #create empty dict for later use

#g is the whole text file, line is each line, and word is each word. i think thats how it lines up anyway
with open ('gba.txt', 'r') as g:
    for line in g:
        for word in line.split():
            noPuncText = word.replace(",", "").replace(".", "") #replaces each comma and period with whitespace
            cleanText = noPuncText.lower() #makes everything lowercase
            allText[cleanText] = allText.get(cleanText, 0) + 1
                        
allItems = allText.items()
print(allItems)