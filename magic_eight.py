from random import randint

def askUser():
	x = str(input("What is your question?"))
	return x

b = askUser()

def answerUser():
	x = randint(0,9)
	
	answers = ['Reply hazy, try again', 'Ask again later.','Better not tell you now.','Cannot predict now.',
		   'Concentrate and ask again.',"Don't count on it.",'My reply is no.','My sources say no.',
		   'Outlook not so good.','Very doubtful.']
	
	print(answers[x])
