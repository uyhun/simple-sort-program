"""
Creating the get_valid_input funciton. 

Check for valid arguments.
Get user_input.
Convert user input to appropriate type.
Check that user input matches constraints passed in as arguments (e.g. min, max, etc.)
"""
#What happens if I pass a string to min/max or not a type to type?
def get_valid_input(prompt, type_=None, min_=None, max_=None, range_=None, re_=None):
	if min_ is not None and max_ is not None and min > max:
		pass # code for min > max case. (Invalid arguments).

	while True:
		user_input = input(prompt) # prompts the user for input.

		#checks for appropriate input type by attempting to typecast user_input.
		if type_ is not None:
			try:
				user_input = type_(user_input)#attempts to typecast user_input
			except Exception, e:
				print("There's an exception!")
				raise e
		#checks that user_input is >= min.
		elif min_ is not None and user_input < min_:
			pass
		#checks that user_input is <= max.
		elif max_ is not None and user_input > max_:
			pass
		#checks that user_input is valid option from a list.
		elif range_ is not None and user_input not in range_:
			pass
		#checks that user_input is of the right format by comparing to a 
		elif re_ is not None:
			pass

#	if min_ is not None and max_ is not None and min > max:
#		pass #add code to manage min>max situation. 
#	while True:
#		if type_ is not None:
#			try:
#				user_input = type_(user_input)
#			except Exception:
#				print(e)