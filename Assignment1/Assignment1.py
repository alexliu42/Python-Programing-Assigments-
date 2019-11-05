def printEvenNumbers():
	userInput = input("Please enter a number: ")
	while userInput.isdigit() != 1:
		 userInput = input("Invalid input format, Please re-enter a number: ")
	print("The even number/numbers between zero and the number you entered are")
	for i in range (0, int(userInput)+1):	
		if i % 2 == 0:
			print(i)

def returnEvenNumbers():
	evenNumbers = []
	userInput = input("Please enter a number: ")
	while userInput.isdigit() != 1:
		 userInput = input("Invalid input format, Please re-enter a number: ")	
	print("The even number/numbers returning from the list between zero and the number you entered are")
	for i in range (0, int(userInput)+1):	
		if i % 2 == 0:
			evenNumbers.append(i)
	return evenNumbers

def returnAllNumbers():
	return [i for i in range (0, int(input("Please enter a numebr: "))+1)]
	
returnAllNumbersLambda = lambda: [i for i in range (0, int(input("Please enter a numebr: "))+1)] 

def returnEveryOtherLetter():
	sliceMe = []
	sliceMe = input("Please enter string, sliceMe: ")
	return sliceMe[::2]


printEvenNumbers()
print(returnEvenNumbers())
print("The numbers returning from the list between zero and your input are: " + str(returnAllNumbers()))
print("(Lambda function) The numbers returning from the list between zero and your input are: " + str(returnAllNumbersLambda()))
print("The every other letters returning from the list are: " + returnEveryOtherLetter())