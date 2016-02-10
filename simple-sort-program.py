from mymethods import get_valid_input
from random import randint
MIN_RAND = 0
MAX_RAND = 100

#Runing tests on the get_valid_input function.
print("Welcome to the simple-sort-program.")
while True:
	play_program = get_valid_input("Would you like to play? (Y, N): ", str.lower, range_=('y', 'n'))
	if play_program == 'y':
		lst_len = get_valid_input("How many numbers would you like to sort? :", int, 1)
		lst = []
		for i in range(lst_len):
			lst.append(randint(MIN_RAND, MAX_RAND))

		print(lst)
	else:
		print("Thanks for visiting!")
		break