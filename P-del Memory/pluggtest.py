difficulty =4
allWords = []  # empty list where all words from textfile memorywords will be added, word for word.
infile = open("toptenhighscore.txt", "r")


load_profile = open('toptenhighscore.txt', "r")
read_it = infile.read()
for line in read_it.splitlines():
    if len(line) <=difficulty:
        allWords.append(line)
    else:
        pass
print(allWords)

for words in allWords:
    if len(words) == difficulty:
        pass
    elif len(words) == difficulty-1:
        words += " "
    elif len(words) == difficulty-2:
        words += " "*2




print(allWords)


