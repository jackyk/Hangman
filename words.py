import random
words= [line.strip() for line in open("words.txt")]
myChosen = random.choice(words)
print myChosen

