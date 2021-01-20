



def integers_only_input():			# Done
	# accept integers only (including negative numbers)
	# no floats or any other data types
	# display error message if empty input
	# return type: int (negative int if input is negative int)
	while True:
		try:
			return int(input("Enter integer: ").strip())
		except ValueError:
			print("Please enter integers only!")


def integers_only_input_clean():	# Done
	# accept integers only (including negative numbers)
	# no floats or any other data types
	# re-prompt if empty input
	# return type: int (negative int if input is negative int)
	while True:
		number = input("Enter integer: ").strip()
		if number:
			try:
				return int(number)
			except ValueError:
				print("Please enter integers only!")


def none_zero_integers_input_only():		# Done
	# accept integers only (including negative numbers)
	# no floats or any other data types
	# display error message if empty input
	# display error message if input == 0
	# return type: int (negative int if input is negative int)
	while True:
		try:
			number = int(input("Enter (none zero) integer: ").strip())
			try:
				1 / number
				return number
			except ZeroDivisionError:
				print("Integer cannot be zero!")
		except ValueError:
			print("Please enter integers only!")


def none_zero_integers_input_only_clean():	# Done
	# accept integers only (including negative numbers)
	# no floats or any other data types
	# re-prompt if empty input
	# display error message if input == 0
	# return type: int (negative int if input is negative int)
	while True:
		number = input("Enter (none zero) integer: ").strip()
		if number:
			try:
				int(number)
				try:
					1 / int(number)
					return int(number)
				except ZeroDivisionError:
					print("Integer cannot be zero!")
			except ValueError:
				print("Please enter integers only!")


def yes_or_no_input_only():			# Done
	# accept "y" or "n" only
	# display error message if empty input
	# display error message if input != "y" or "n"
	# return True for "y" and False for "n"
	while True:
		theDamnAnswer = input("Answer the damn question, (y/n): ").strip().lower()
		if theDamnAnswer == "y" or theDamnAnswer == "n":
			return True if theDamnAnswer == "y" else False
		else:
			print('Please answer with "y" or "n" only!')


def yes_or_no_input_only_clean():	# Done
	# accept "y" or "n" only
	# re-prompt if empty input
	# display error message if input != "y" or "n"
	# return True for "y" and False for "n"
	while True:
		answer = input("Are you going to answer this question or not?, (y/n): ").strip().lower()
		if answer:
			if answer == "y" or answer == "n":
				return True if answer == "y" else False
			else:
				print('Please answer with "y" or "n" only!')


def letters_only_input():
	# accept letters only input
	# display error message if empty input
	# display error message if input is not composed of letters only
	# return type: str
	while True:
		userInput = input("Do you like letter jackets?: ")
		if userInput.isalpha():
			return userInput
		else:
			print("Please enter letters only!")


def letters_only_input_clean():
	# accept letters only input
	# re-prompt if empty input
	# display error message if input is not composed of letters only
	# return type: str
	while True:
		userInput = input("Do you like letter jackets?: ")
		if userInput:
			if userInput.isalpha():
				return userInput
			else:
				print("Please enter letters only!")





