def askUser():
	x = str(input("What is your question?"))
	return x

b = askUser()

def checkQuestion(string):
	if string[-1] == '?':
		return true
	else:
		print ("I’m sorry, I can only answer questions.")
