import random

RAND_MIN = 0
RAND_MAX = 100
print("Welcome to Simple Sort Program")
start = input("Would you like to play? (Y/N): ").lower()
while start != 'y' and start != 'n':
	print("Sorry, that's now a valid input.")
	start = input ("Please try again. (Y/N): ").lower()

arrSize = int(input("How many numbers would you like to sort? (1-100):"))
arr = []
for i in range(0, arrSize): 
	print(i)
	arr.append(random.randint(RAND_MIN, RAND_MAX))

print("done with loop")
print(arr)
