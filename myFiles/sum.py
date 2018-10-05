def sum(FirstNumber, SecondNumber):
	Result = 0
	if (FirstNumber < 0) or (SecondNumber < 0):
		print('Incorrect input number(s)')
		return None
	if (FirstNumber > 0) and (SecondNumber > 0):
		Result += 2
		Result += sum(FirstNumber - 1, SecondNumber - 1)
	elif (FirstNumber == 0):
		if (SecondNumber == 0):
			return Result
		Result += 1
		Result += sum(0, SecondNumber - 1)
	elif (SecondNumber == 0):
		if (FirstNumber == 0):
			return Result
		Result += 1
		Result += sum(FirstNumber - 1, 0)
	return Result
