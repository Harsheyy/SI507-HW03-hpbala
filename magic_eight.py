from random import randint

def askUser():
	x = input("What is your question?    ")
	return str(x)


#b = askUser()

check = False

def checkQuestion(string):
	if string[-1] == '?':
		check = True
		return check
	else:
		print ("I'm sorry, I can only answer questions.")
		check = False
		return check

def answerUser():
	x = randint(0,19)
	list = ["It is decidedly so.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
          "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
          'Reply hazy, try again', 'Ask again later.','Better not tell you now.','Cannot predict now.',
		      'Concentrate and ask again.',"Don't count on it.",'My reply is no.','My sources say no.',
		      'Outlook not so good.','Very doubtful.']
	print(list[x])

b = askUser()
while b != 'quit':
	while checkQuestion(b) == False:
		b = askUser()
	answerUser()

