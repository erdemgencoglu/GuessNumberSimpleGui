import simplegui
import random

global rand
global count
count=7

def new_game():
	global rand
	global count
	count=7
	print "New game.Range is from 0 to 100"
	print "Number of remaining guesses is",count
	rand=random.randrange(1,100)


def range100():
	global count
	count=7
	new_game()

def range1000():
	global rand
	global count
	count=7
	print "New game.Range is from 0 to 1000"
	print "Number of remaining guesses is",count
	rand=random.randrange(1,1000)

def get_inputGuess(guessnumber):
	global rand
    global count 
    count-=1
    print "Guess was ",guessnumber
    print "Number of remaining guesses is",count
    
    if rand==int(guessnumber):
        print "Correct"
    elif rand<int(guessnumber):
        print "Lower!"
    elif rand>int(guessnumber):
        print "Higher!"
    if count==0:
        print "Number of guesses finished"
        print 
        new_game()

#create frame area
f=simplegui.create_frame("GuessNumberGame",200,200)

f.add_button("Range is [0, 100)",range100,200)
f.add_button("Range is [0, 1000)",range1000,200)
f.add_input("Enter a guess",get_inputGuess,200)


f.start()
new_game()

