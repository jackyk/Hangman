import random
from hanggraphics import hang
# word = ["test", "create","dictate","reserve","honest"]
word = [line.strip() for line in open("words.txt")]
myChosen = random.choice(word)
dash_item = ["_ " for char in myChosen]
userSaid = ""
print "Guess a letter that forms the following word: "
print "Your word looks like this: ", dash_item
#
# def done(userinput, myChosen):
#     for letter in myChosen:
#         if letter not in userinput:
#             return False
#     return True
def showhang(hang,userGuess):
    return hang[userGuess -8]

def hangman():
    global myChosen, dash_item, userSaid
    userGuess = 1
    while userGuess <= 8:
        userinput = raw_input("Your Guess: ")
        if userinput in myChosen:
            dash_item = [char if char == userinput or char in userSaid else "_ " for char in myChosen] #creates a list and checks when all that happens
            dash_item = "".join(dash_item)
            print dash_item
        else:
            print "Item not in word: "+showhang(hang,userGuess)
            print dash_item
        userSaid = userSaid+userinput

        if len(userinput) != 1 or len(userinput) == 0   :
            print "Try again"
        else:
            pass
        # if done(userinput, myChosen):
        #     print "Well done" + myChosen
        userGuess+=1
hangman()
























# #C
# def count_intersections(userinput, myChosen):
#     count = 0
#     indices = []
#     while count < len(myChosen_list):
#         if userinput == myChosen[count]:
#             indices.append(count)
#         count+=1
#     return indices


# def replacing_guess(indices,userinput,dash_item):
#     for x in indices:
#         myChosen[:int(x)] +dash_item + userinput
        # indices = count_intersections(userinput, myChosen)
        # dash_item = replacing_guess(indices,userinput,dash_item)
