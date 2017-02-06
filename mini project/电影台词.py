#coding:utf-8

blank = ['__1__','__2__','__3__','__4__'] #for replace

easy_level = blank[0] + ' was like a box of '\
 + blank[1] +', never ' + blank[2] + ' what you\'re gonna ' + blank[3] +'.'
easy_answers = ['life', 'chocolate', 'know', 'get']
medium_level = 'A census taker once tried to ' + blank[0] +' me.I ate his '\
 + blank[1] + ' with some ' + blank[2] + ' and a nice ' + blank[3] + '.'
medium_answers = ['test', 'liver', 'fava beans', 'chianti']
hard_level = 'I figure life is a ' + blank[0] + ' and I don’t intend on ' + blank[1] +' it. You \
never know what hand you’re going to get ' + blank[2] + ' next. You learn to take life as it \
' + blank[3] + ' at you.'
hard_answers = ['gift', 'wasting', 'dealt', 'comes']

#answers and quiz
#print easy_level

def welcome(): #choose level and explain the game
	print 'Welcome to the movie quotes quiz, you gonna fill in some quotes that is form \
classical movies, now type \'easy\' or \'medium\' or \'hard\' to select a level.'
	print '*easy*|**medium**|***hard***'

welcome()

def levels(): # select the level, return a list
	user_level = raw_input() 
	levels = ['easy', 'medium', 'hard']
	while user_level not in levels:
		print 'try to spell \'easy\' or \'medium\' or \'hard\''
		user_level = raw_input()
	if user_level == levels[0]:
		return easy_level
	elif user_level == levels[1]:
		return medium_level
	elif user_level == levels[2]:
		return hard_level

def show_quiz(level):  # outputs quiz and answers
    if level == easy_level:
        return easy_answers
    elif level == medium_level:
        return medium_answers
    elif level == hard_level:
        return hard_answers

def ask_question(quiz, answers): #judge
    index = 0
    while index < len(answers):
        print quiz
        user_answer = raw_input('Answer: ')
        while user_answer not in answers:
            print 'Wrong answer! Please try again.'
            user_answer = raw_input('Answer: ')
        quiz = quiz.replace(blank[index], answers[index])
        print 'correct!'
        index = index + 1

''' #try to make a hint function but failed
def hint():
    hint = 0
    a = quiz_answers
    s = a[hint]
    while hint < len(s):
        print 'hint: the %d letter is ' % (hint + 1) + s[hint]
    hint = hint + 1
    print 'the word is ' + answers[index]
'''

def begin_quiz():  # start
    #hint = hint()
    level = levels()  # level = easy_quiz
    quiz_answers = show_quiz(level) # easy_answers = show_quiz(level)
    ask_question(level, quiz_answers)
begin_quiz()

print 'Thank you for playing'