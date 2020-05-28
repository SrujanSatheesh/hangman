from random import randint
from graphics import *


def getInfile():
	try:

		with open('wordlist.txt', 'r'): infile_name = 'wordlist.txt'
	except:

		found_file = False
		infile_name = input('Please specify a text file containing a list of words for the Hangman game to choose from (include the full file path if the file is in a different directory than the Hangman program): ')

		while not(found_file):
			try:
				with open(infile_name, 'r'): found_file = True
			except:
				infile_name = input('\n{0} was not found!\n\nPlease try again, or specify a different file (include the full file path if the file is in a different directory than the Hangman program): '.format(infile_name))

	return infile_name

def chooseWord(infile_name):
	infile = open(infile_name, 'r')
	wordlist = infile.readlines()
	total_words = len(wordlist)
	random_num = randint(0, total_words - 1)

	chosen_word = wordlist[random_num].replace('\n', '')
	word_len = len(chosen_word)
	return chosen_word, word_len


def drawPiece(strike, win, win_width, win_height, win_hangmanpic):
	hangman_yaxis = win_width / 2.2
	if strike == 1:

		line1 = Line(Point(win_width - win_width / 3, 100), Point(win_width - win_width / 3, 300))
		line1.draw(win)
		win_hangmanpic.append(line1)
		line2 = Line(Point(win_width - win_width / 3, 300), Point(hangman_yaxis, 300))
		line2.draw(win)
		win_hangmanpic.append(line2)
		line3 = Line(Point(hangman_yaxis, 300), Point(hangman_yaxis, 270))
		line3.draw(win)
		win_hangmanpic.append(line3)
	elif strike == 2:

		circle4 = Circle(Point(hangman_yaxis, 254), 16)
		circle4.draw(win)
		win_hangmanpic.append(circle4)
	elif strike == 3:

		line5 = Line(Point(hangman_yaxis, 238), Point(hangman_yaxis, 180))
		line5.draw(win)
		win_hangmanpic.append(line5)
	elif strike == 4:

		line6 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis - 20, 200))
		line6.draw(win)
		win_hangmanpic.append(line6)
	elif strike == 5:

		line7 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis + 20, 200))
		line7.draw(win)
		win_hangmanpic.append(line7)
	elif strike == 6:

		line8 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis - 15, 135))
		line8.draw(win)
		win_hangmanpic.append(line8)
	elif strike == 7:

		line9 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis + 15, 135))
		line9.draw(win)
		win_hangmanpic.append(line9)

		line10 = Line(Point(hangman_yaxis + 7, 260), Point(hangman_yaxis + 2, 255))
		line10.draw(win)
		win_hangmanpic.append(line10)
		line11 = Line(Point(hangman_yaxis + 2, 260), Point(hangman_yaxis + 7, 255))
		line11.draw(win)
		win_hangmanpic.append(line11)
		line12 = Line(Point(hangman_yaxis - 7, 260), Point(hangman_yaxis - 2, 255))
		line12.draw(win)
		win_hangmanpic.append(line12)
		line13 = Line(Point(hangman_yaxis - 2, 260), Point(hangman_yaxis - 7, 255))
		line13.draw(win)
		win_hangmanpic.append(line13)

		line14 = Line(Point(hangman_yaxis - 7, 247), Point(hangman_yaxis + 7, 247))
		line14.draw(win)
		win_hangmanpic.append(line14)


def main(win, infile_name):

	if not(infile_name):
		infile_name = getInfile()

	word, word_len = chooseWord(infile_name)

   
	grid = '__'
	for i in range(word_len - 1):
		grid = grid + ' __'


	win_width = 500
	win_height = 460
	if not(win):

		win = GraphWin("Hangman", win_width, win_height)
		win.setCoords(0, 0, win_width, win_height)


	win_message = Text(Point(win_width / 2, 70), "Let's play! Guess a letter below to see if it's in the word.")
	win_message.setStyle('bold')
	win_message.draw(win)
	win_ground = Line(Point(60, 100), Point(win_width - win_width / 10, 100))
	win_ground.draw(win)
	win_grid = Text(Point(win_width / 2, win_height - 70), grid)
	win_grid.draw(win)


	win_guesstxt = Text(Point(win_width / 2 - 35, 30), "Type a letter:")
	win_guesstxt.draw(win)
	win_guessinput = Entry(Point(win_width / 2 + 30, 28), 2)
	win_guessinput.draw(win)
	win_guessinput.setText('')


	win_butguess = Rectangle(Point(win_width / 2 + 55, 43), Point(win_width / 2 + 130, 13))
	win_butguess.setFill("yellow")
	win_butguess.setOutline("red")
	win_butguess.draw(win)
	win_butguess_label = Text(Point(win_width / 2 + 94, 28), 'Guess it!')
	win_butguess_label.setTextColor("red")
	win_butguess_label.draw(win)

	strikes = 0
	guessed_letters = []
	win_hangmanpic = []
	game_won = False
	while strikes < 7 and game_won == False:

		p = win.getMouse()

		if p.getX() < win_width / 2 + 55 or p.getX() > win_width / 2 + 130 or p.getY() < 13 or p.getY() > 43:
			continue


		guess = win_guessinput.getText().lower()
		win_guessinput.setText('')
		if guess == ' ' or guess == '' or len(guess) != 1:
			if len(guess) != 1:
				win_message.setText("Please only guess a single letter at a time. Try again!")
			continue


		if guess in word.lower() and not(guess in guessed_letters):
			guessed_letters.append(guess)
			grid = word
			for letter in word:
				if (not (letter.lower() in word) or not(letter.lower() in guessed_letters)) and letter != ' ':
					grid = grid.replace(letter, ' __ ')

				win_grid.setText(grid)

			if grid == word:
				game_won = True
			else:
				win_message.setText("Nice! {0} is in the word. Try another letter.".format(guess.upper()))
		elif guess in guessed_letters:

			win_message.setText("You've already guessed {0}. Try another letter.".format(guess.upper()))
		else:

			guessed_letters.append(guess)
			strikes = strikes + 1
			win_message.setText('{0} is a wrong guess! Try another letter.'.format(guess.upper()))
			drawPiece(strikes, win, win_width, win_height, win_hangmanpic)


	win_guesstxt.undraw()
	win_guessinput.undraw()
	win_butguess.undraw()
	win_butguess_label.undraw()
	win_message.move(0, -10)
	win_grid.setText(word.upper())
	win_grid.setStyle('bold')
	win_grid.setSize(16)


	if game_won == True:
		win_message.setText("Congrats! You've guessed the word correctly.")
		win_message.setTextColor(color_rgb(0, 120, 0))
		win_grid.setTextColor(color_rgb(0, 120, 0))

		for hm_obj in win_hangmanpic:
			hm_obj.undraw()
		win_hangmanpic = []

		circle1 = Circle(Point(win_width / 2, 240), 110)
		circle1.setOutline(color_rgb(0, 120, 0))
		circle1.setFill(color_rgb(126, 236, 53))
		circle1.draw(win)
		win_hangmanpic.append(circle1)
		eye1 = Circle(Point(win_width / 2 - 40, 285), 20)
		eye1.setOutline(color_rgb(0, 120, 0))
		eye1.draw(win)
		win_hangmanpic.append(eye1)
		eye2 = eye1.clone()
		eye2.move(80, 0)
		eye2.draw(win)
		win_hangmanpic.append(eye2)
		eye1_inner = Circle(Point(win_width / 2 - 40, 285), 5)
		eye1_inner.setFill(color_rgb(0, 120, 0))
		eye1_inner.setOutline(color_rgb(0, 120, 0))
		eye1_inner.draw(win)
		win_hangmanpic.append(eye1_inner)
		eye2_inner = eye1_inner.clone()
		eye2_inner.move(80, 0)
		eye2_inner.draw(win)
		win_hangmanpic.append(eye2_inner)
		mouth = Circle(Point(win_width / 2, 200), 50)
		mouth.setFill(color_rgb(0, 120, 0))
		mouth.setOutline(color_rgb(0, 120, 0))
		mouth.draw(win)
		win_hangmanpic.append(mouth)
		mouth_cover = Rectangle(Point(win_width / 2 - 50, 200), Point(win_width / 2 + 50, 250))
		mouth_cover.setFill(color_rgb(126, 236, 53))
		mouth_cover.setOutline(color_rgb(126, 236, 53))
		mouth_cover.draw(win)
		win_hangmanpic.append(mouth_cover)
	else:
		win_message.setText("Sorry! You didn't completely guess the word.")
		win_message.setTextColor(color_rgb(170, 0, 0))
		win_grid.setTextColor(color_rgb(170, 0, 0))

		i = 0
		for hm_obj in win_hangmanpic:
			if i == 3:

				hm_obj.setOutline(color_rgb(170, 0, 0))
			else:
				hm_obj.setFill(color_rgb(170, 0, 0))
			# Increment the index counter
			i = i + 1


	win_butagain = Rectangle(Point(win_width - 90, 30), Point(win_width, 0))
	win_butagain.setFill(color_rgb(126, 236, 53))
	win_butagain.setOutline(color_rgb(0, 110, 0))
	win_butagain.draw(win)
	win_butagain_label = Text(Point(win_width - 45, 15), 'Play again?')
	win_butagain_label.setTextColor(color_rgb(0, 110, 0))
	win_butagain_label.draw(win)


	win_butquit = Rectangle(Point(4, 30), Point(54, 0))
	win_butquit.setFill(color_rgb(255, 177, 177))
	win_butquit.setOutline(color_rgb(170, 0, 0))
	win_butquit.draw(win)
	win_butquit_label = Text(Point(29, 15), 'Quit')
	win_butquit_label.setTextColor(color_rgb(170, 0, 0))
	win_butquit_label.draw(win)


	opt_selected = False
	while not(opt_selected):
		p = win.getMouse()
		if p.getX() >= (win_width - 90) and p.getY() <= 30:
			
			opt_selected = 1
		elif p.getX() <= 54 and p.getY() <= 30:

			opt_selected = 2


	if opt_selected == 1:

		graphic_objs = [win_message, win_ground, win_grid, win_butagain, win_butagain_label, win_butquit, win_butquit_label, win_hangmanpic]
		for obj in graphic_objs:
			if obj == win_hangmanpic:
				for hm_obj in win_hangmanpic:
					hm_obj.undraw()
			else:
				obj.undraw()

		main(win, infile_name)
	else:

		win.close()

main(False, False)
