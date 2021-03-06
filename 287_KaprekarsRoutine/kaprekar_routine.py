'''
/r/DailyProgrammer Challenge #287 - Kaprekar's Routine

Given a 4-digit number, return its largest digit

Bonus 1: Given a 4-digit number, return them in descending order
Bonus 2: Write a function that counts the number of iterations in Kaprekar's Routine, which is as follows.
\nGiven a 4-digit number that has at least two different digits, take that number's descending digits, and subtract that number's ascending digits. For example, given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.

'''

import os.path
import random

'''
Creates an input file (if it doesn't already exists)
with a bunch of random numbers to run as input
'''
def create_input_file():
	if(os.path.exists("./input.txt")):
		return
	else:
		with open("input.txt", "w") as f:
			for i in range(0, 10000):
				num = random.randrange(100, 9999)
				f.write(str(num) + "\n")
			f.close()
		return


def desc_digits(number):
	separate_numbers = [int(i) for i in str(number)]
	separate_numbers.sort(reverse=True)

	a = ''.join(str(num) for num in separate_numbers) 	# Can also use map here, although i think this is more efficient
	#print("desc_digits({0}) -> {1}".format(number, a))

	return a

def asc_digits(number):
	separate_numbers = [int(i) for i in str(number)]
	separate_numbers.sort()

	a = ''.join(str(i) for i in separate_numbers)
	#print("asc_digits({0}) -> {1}".format(number, a))

	return a

def kaprekar_routine(number):
	kap_constant = 6174
	iterations = 0

	print("---Kaprekar Routine: {0}---".format(number))
	while(number != kap_constant):
		asc_num = int(asc_digits(number))
		desc_num = int(desc_digits(number))

		number = desc_num - asc_num
		iterations += 1

	print("iterations: {0}".format(iterations))
	return iterations

def largest_digit(number):
	if(number > 9999):
		print("The input has to be 4-digit or less")
		return

	#Using list comprehension:
	separate_numbers =[int(i) for i in str(number)]

	# Using a for loop
	# separate_numbers = []
	# for i in str(number):
	# 	separate_numbers.append(int(i))	

	largest = int(max(separate_numbers))
	print("largest_digit({0}) -> {1}".format(number, largest))

	return largest

print("/r/DailyProgrammer Challenge #287 - Kaprekar's Routine")

# create_input_file()
# with open("input.txt", "r") as f:
# 	for line in f:
# 		largest_digit(int(line))

largest_digit(3456)
largest_digit(3222)
largest_digit(3574)
largest_digit(3333)
largest_digit(12345)
largest_digit(2000)
largest_digit(123)

desc_digits(4562)
desc_digits(3445)
desc_digits(1234)
desc_digits(6758)

asc_digits(3461)
asc_digits(9876)
asc_digits(3433)

kaprekar_routine(7149)
kaprekar_routine(9218)
