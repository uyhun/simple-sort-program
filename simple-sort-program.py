"""
Creating the get_valid_input funciton. 

Check for valid arguments.
Get user_input.
Convert user input to appropriate type.
Check that user input matches constraints passed in as arguments (e.g. min, max, etc.)
"""

def get_valid_input(prompt, type_=None, min_=None, max_=None, range_=None, re_=None):
	if min_ is not None and max_ is not None and min > max:
		pass # code for min > max case. (Invalid arguments).

	while True:
		user_input = input(prompt) # prompts the user for input.
		if type_ is not None:
			try:
				pass
			except Exception, e:
				raise e
		elif min is not None:
			pass
		elif max_ is not None:
			pass
		elif range is not None:
			pass
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