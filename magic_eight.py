from random import randint

def askUser():
	x = str(input("What is your question?"))
	return x

b = askUser()

def answerUser():
	x = randint(0,9)
	list = ["It is decidedly so.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]
	return list[x]	
