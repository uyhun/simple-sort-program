#mymethods for simple-sort-program

#get_valid_input prompts the terminal user for an input until a valid input is entered.
def get_valid_input(prompt, type_=None, min_=None, max_=None, range_=None, re_=None):
	if min_ is not None and max_ is not None and min_ > max_:
		raise ValueError("min_ must be less than or equal to max_.")
	while True:
		user_input = input(prompt) # prompts the user for input.
		#checks for appropriate input type by trying to typecast user_input.
		if type_ is not None:
			try:
				user_input = type_(user_input)#attempts to typecast user_input
			except ValueError:
				print("Input must be of type {0}.".format(type_.__name__))
				continue
		#checks that the user_input is >=min
		elif min_ is not None and user_input < min_:
			print("Input must be greater or equal to {0}.".format(min_))
		#checks that user_input is <= max.
		elif max_ is not None and user_input > max_:
			print("Input must be less than or equal to {0}.".format(max_))
		#checks that user_input is valid option from a list.
		elif range_ is not None and user_input not in range_:
			if isinstance(range_, range):
				template = "Input must be between {0.start} and {0.stop}."
				print(template.format(range_))
			else:
				template = "Input must be {0}."
				if len(range_)==1:
					print(template.format(*range_))
				else:
					print(template.format(" or ".join((", ".join(map(str, range_[:-1])), str(range_[1])))))
		#checks that user_input is of the right format by comparing to a regular expression
		elif re_ is not None:
			pass
		else:
			return user_input