Stack Exchange Inbox Reputation and Badges sign up log in tour help

Search Q&A

Stack Overflow
Questions

Jobs

Documentation

Tags

Users

Badges

Ask Question
Dismiss
Announcing Stack Overflow Documentation
We started with Q&A. Technical documentation is next, and we need your help.

Whether you're a beginner or an experienced developer, you can contribute.

Sign up and start helping →  Learn more about Documentation →
Hangman game code

up vote
0
down vote
favorite
I would like to get some help regarding the hangman game. I've created this piece of code and have spent a lot of time trying to refine it but I still can't get the correct output. Would really appreciate your help!

word = choose_word(wordlist)
letters = 'abcdefghijklmnopqrstuvwxyz'
numLetters = len(word)
print numLetters

import re


def hangman(word, numLetters):
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', numLetters, 'letters long'
    remainingGuesses = 8
    print 'You have', remainingGuesses, 'guesses left.'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print 'Available letters:', letters
    guess = raw_input("Please guess a letter:")

    def filled_word(wordy, guessy):
        emptyWord = ['_']*numLetters
        if wordy.find(guessy) != -1:
            position = [m.start() for m in re.finditer(guessy, wordy)]
            for x in position:
                emptyWord[x] = guessy
            strWord = ''.join(emptyWord)
            print 'Good guess =', strWord


        else:
            strWord = ''.join(emptyWord)
            print 'Oops! That letter is not in my word:', strWord

    filled_word(word, guess)
    emptyWord =  ['_']*numLetters
    print 'emptyWord =', ['_']*numLetters

    while '_' in emptyWord and remainingGuesses>0:
        remainingGuesses -= 1
        print 'You have', remainingGuesses, 'guesses left'
        letters = 'abcdefghijklmnopqrstuvwxyz'

        def unused_letters(letters):
            letters = 'abcdefghijklmnopqrstuvwxyz'
            unusedLetters = str(list(letters).remove(guess))
            letters = unusedLetters
            return unusedLetters

        letters =  unused_letters(letters)
        print 'Available letters:', letters
        guess = raw_input("Please guess a letter:")

        if word.find(guess) != -1:
            position = [m.start() for m in re.finditer(guess, word)]
            for x in position:
                emptyWord[x] = guess
                strWord = ''.join(emptyWord)
                print 'Good guess ='+strWord
                emptyWord = list(strWord)

        else:
            strWord = ''.join(emptyWord)
            print 'Oops! That letter is not in my word:', strWord


print hangman(word, numLetters)
print '___________'
print 'Congratulations, you won!'
So the problem is that when I run this, the code runs smoothly until from the second guess onwards, I get Available letters = None instead of the specific letters.

Also, the letter I guess which does appear in the word is not stored. i.e. in guess 1, the code returns the word (for example) 'd____', but in guess 2, upon guessing 'e', the code returns the word 'e_' instead of 'd_e__'. Is it because of the assignment of variables? Of local and global variables? Am quite confused about this.

Would really appreciate the help! Thanks a lot! :)

python variables
shareimprove this question
asked Apr 30 '14 at 13:29

inggumnator
1295

Have you tried stepping through your code with pdb/ipdb to see when things change? – dutt Apr 30 '14 at 13:36

Sorry I'm really new to python, what do you mean by using pdb/ipdb to see when things change? – inggumnator Apr 30 '14 at 15:26
add a comment
3 Answers
active oldest votes
up vote
1
down vote
def choose_word():
    word = 'alphabeth'
    return {'word':word, 'length':len(word)}

def guess_letter(word_, hidden_word_, no_guesses_, letters_):
    print '---------------------------------------'
    print 'You have', no_guesses_, 'guesses left.'
    print 'Available letters:', letters_

    guess = raw_input("Please guess a letter:")
    guess = guess.lower()

    if guess in letters_:
        letters_ = letters_.replace(guess, '')

        if guess in word_:
            progress = list(hidden_word_)
            character_position = -1
            for character in word_:
                character_position += 1
                if guess == character:
                    progress[character_position] = guess
            hidden_word_ = ''.join(progress)
            print 'Good guess =', hidden_word_
        else:
            print 'Oops! That letter is not in my word:', hidden_word_
            no_guesses_ = no_guesses_ - 1
    else:
        print 'The letter "', guess, '" was already used!'
        no_guesses_ = no_guesses_ - 1

    if hidden_word_ == word_:
        print 'Congratulations, you won!'
        return True
    if no_guesses_ == 0 and hidden_word_ != word_:
        print 'Game over! Try again!'
        return False
    return guess_letter(word_, hidden_word_, no_guesses_, letters_)

def hangman():
    hangman_word = choose_word()
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', hangman_word['length'], 'letters long.'

    hidden_word = ''.join(['_'] * hangman_word['length'])
    no_guesses = 8
    letters = 'abcdefghijklmnopqrstuvwxyz'

    guess_letter(hangman_word['word'], hidden_word, no_guesses, letters)

hangman()
shareimprove this answer
answered May 1 '14 at 10:17

StefanNch
1,4131225
add a comment

up vote
0
down vote
There are multiple errors in the code. Here it is corrected:-

import re

def unused_letters( letters, guess ): # your main problem is corrected here.
    unusedLetters = list( letters )
    unusedLetters.remove( guess )

    letters = ''.join( unusedLetters )
    return letters

def filled_word( wordy, guessy ):
    if wordy.find( guessy ) != -1:
        position = [m.start() for m in re.finditer( guessy, wordy )]
        for x in position:
            filled_word.emptyWord[x] = guessy
        strWord = ''.join( filled_word.emptyWord )
        print 'Good guess.'
        print 'Current word: %s' % ''.join( filled_word.emptyWord )
    else:
        strWord = ''.join( filled_word.emptyWord )
        print 'Oops! That letter is not in my word:', strWord

def hangman( word, numLetters ):  # you dont need the previous check. Let all be done in the main loop
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', numLetters, 'letters long'
    remainingGuesses = 8
    letters = 'abcdefghijklmnopqrstuvwxyz'
    try:
        # # memoizing the current word. for more info, try to understand that functions are
        # # also objects and that we are assigning a new attribute the function object here.
        filled_word.emptyWord
    except:
        filled_word.emptyWord = ['_'] * numLetters
    while '_' in filled_word.emptyWord and remainingGuesses > 0:

        print 'You have', remainingGuesses, 'guesses left'

        print 'Available letters:', letters
        guess = raw_input( "Please guess a letter:" )
#         print 'guess: %s' % guess
        if guess in letters:
            filled_word( word, guess )
            letters = unused_letters( letters, guess )
        else:
            print 'You guessed: %s, which is not in Available letters: %s' % ( guess, ''.join( letters ) )
            print 'Current word: %s' % ''.join( filled_word.emptyWord )

        remainingGuesses -= 1

word = "godman"

print hangman( word, numLetters = len( word ) )
if '_' in filled_word.emptyWord:
    print 'Ahh ! you lost....The hangman is hung'
else:
    print 'Congratulations, you won!'
You can still make it better by checking if the remaining number of guesses are less than the letters to be filled, and take a decision on whether to fail the player or allow it to continue playing.

shareimprove this answer
edited May 1 '14 at 7:09
answered Apr 30 '14 at 13:36

GodMan
1,091826

Thanks for the quick reply! Though the remove method only works for lists so it is still necessary to convert the string, letters, into a list. I'm still having the problem of the letter which I guessed showing up immediately after that guess but then disappearing in the subsequent guesses. Do you have any idea why is that so? – inggumnator Apr 30 '14 at 15:28
add a comment
up vote
0
down vote
class Hangman(): def init(self): print "Welcome to 'Hangman', are you ready to die?" print "(1)Yes, for I am already dead.\n(2)No, get me outta here!" user_choice_1 = raw_input("->")

    if user_choice_1 == '1':
        print "Loading nooses, murderers, rapists, thiefs, lunatics..."
        self.start_game()
    elif user_choice_1 == '2':
        print "Bye bye now..."
        exit()
    else:
        print "I'm sorry, I'm hard of hearing, could you repeat that?"
        self.__init__()

def start_game(self):
    print "A crowd begins to gather, they can't wait to see some real"
    print "justice. There's just one thing, you aren't a real criminal."
    print "No, no. You're the wrong time, wrong place type. You may think"
    print "you're dead, but it's not like that at all. Yes, yes. You've"
    print "got a chance to live. All you've gotta do is guess the right"
    print "words and you can live to see another day. But don't get so"
    print "happy yet. If you make 6 wrong guess, YOU'RE TOAST! VAMANOS!"
    self.core_game()

def core_game(self):
    guesses = 0
    letters_used = ""
    the_word = "pizza"
    progress = ["?", "?", "?", "?", "?"]

    while guesses < 6:
        guess = raw_input("Guess a letter ->")

        if guess in the_word and not in letters_used:
            print "As it turns out, your guess was RIGHT!"
            letters_used += "," + guess
            self.hangman_graphic(guesses)
            print "Progress: " + self.progress_updater(guess, the_word, progress)
            print "Letter used: " + letters_used
        elif guess not in the_word and not(in letters_used):
            guesses += 1
            print "Things aren't looking so good, that guess was WRONG!"
            print "Oh man, that crowd is getting happy, I thought you"
            print "wanted to make them mad?"
            letters_used += "," + guess
            self.hangman_graphic(guesses)
            print "Progress: " + "".join(progress)
            print "Letter used: " + letters_used
        else:
            print "That's the wrong letter, you wanna be out here all day?"
            print "Try again!"



def hangman_graphic(self, guesses):
    if guesses == 0:
        print "________      "
        print "|      |      "
        print "|             "
        print "|             "
        print "|             "
        print "|             "
    elif guesses == 1:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|             "
        print "|             "
        print "|             "
    elif guesses == 2:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|     /       "
        print "|             "
        print "|             "
    elif guesses == 3:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|     /|      "
        print "|             "
        print "|             "
    elif guesses == 4:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|     /|\     "
        print "|             "
        print "|             "
    elif guesses == 5:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|     /|\     "
        print "|     /       "
        print "|             "
    else:
        print "________      "
        print "|      |      "
        print "|      0      "
        print "|     /|\     "
        print "|     / \     "
        print "|             "
        print "The noose tightens around your neck, and you feel the"
        print "sudden urge to urinate."
        print "GAME OVER!"
        self.__init__()

def progress_updater(self, guess, the_word, progress):
    i = 0
    while i < len(the_word):
        if guess == the_word[i]:
            progress[i] = guess
            i += 1
        else:
            i += 1

    return "".join(progress)
game = Hangman()

shareimprove this answer
answered Nov 8 '15 at 17:59

Nursultan Zhamshitov
1
add a comment
Your Answer



Post Your Answer
By posting your answer, you agree to the privacy policy and terms of service.

Not the answer you're looking for?	Browse other questions tagged python variables or ask your own question.

asked

2 years ago

viewed

288 times

active

9 months ago


Related

-2
Error With My Hangman Game
0
hangman game substituting letters
0
duplicate word in hangman game
0
Problems with my Hangman game (Python)
-7
Hangman Game Python Error
-3
The 'Hangman' game python code testing
1
Python: Hangman game problems
0
Python hangman game. Python 3
-3
Unable to guess a correct letter in a Hangman Game
0
Python hangman game for loop
Hot Network Questions

Are grey squirrels really bad for the overall habitat in Germany?
Tips for improving commute efficiency/comfort?
I am seen by millions
Await your command, what am I?
Is the 2-sphere homeomorphic to a topological group?
more hot questions
question feed
about us tour help blog chat data legal privacy policy work here advertising info mobile contact us feedback
TECHNOLOGY	LIFE / ARTS	CULTURE / RECREATION	SCIENCE	OTHER
Stack Overflow
Server Fault
Super User
Web Applications
Ask Ubuntu
Webmasters
Game Development
TeX - LaTeX
Programmers
Unix & Linux
Ask Different (Apple)
WordPress Development
Geographic Information Systems
Electrical Engineering
Android Enthusiasts
Information Security
Database Administrators
Drupal Answers
SharePoint
User Experience
Mathematica
Salesforce
ExpressionEngine® Answers
more (13)
Photography
Science Fiction & Fantasy
Graphic Design
Movies & TV
Seasoned Advice (cooking)
Home Improvement
Personal Finance & Money
Academia
more (9)
English Language & Usage
Skeptics
Mi Yodeya (Judaism)
Travel
Christianity
Arqade (gaming)
Bicycles
Role-playing Games
more (21)
Mathematics
Cross Validated (stats)
Theoretical Computer Science
Physics
MathOverflow
Chemistry
Biology
more (5)
Stack Apps
Meta Stack Exchange
Area 51
Stack Overflow Careers
site design / logo © 2016 Stack Exchange Inc; user contributions licensed under cc by-sa 3.0 with attribution required
rev 2016.8.18.3903
