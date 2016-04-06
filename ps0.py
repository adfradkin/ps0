#0
def is_even(number):
	'''Takes a non-negative integer as a parameter and returns True if the number is even, False if it is odd.'''
	if number % 2 == 0:
		return True
	else:
		return False
#1
def digit_counter(number):
	'''Takes a non-negative integer as a parameter and returns the number of digits in it.'''
	counter = 0
	while number >= 1:
		number=number / 10
		counter += 1
	return counter
#2
def sum_digit(number):
	'''Takes a non-negative integer as a parameter and returns the sum of its digits.'''
	answer = 0
	while number > 0:
		tempNum = number % 10
		answer += tempNum
		number = (number-tempNum)
		number /= 10
	return answer 
#3
def add_below(number):
	'''Takes a non-negative integer as a parameter and returns 
	the sum of all the integers that are less than the given number.'''
	answer = 0
	while number > 0:
		number -= 1
		answer += number
	return answer
#4
def factorial(number):
	'''Takes a non-negative integer as a parameter and returns its factorial.'''
	answer = 1	
	while number > 0:
		answer *= number
		number -= 1
	return answer
#5
def factor_check(number, factor):
	'''Takes two positive integers as parameters and figures out 
	whether the second number is a factor of the first.'''
	if number % factor == 0:
		return True
	else:
		return False
#6
def prime_check(number):
	'''Takes an integer greater 
	than or equal to 2 as a parameter and returns whether the number is a prime.'''
	primeChecker = number
	while primeChecker>2:
		if number % 2 == 0:
			return False
		for n in range(primeChecker,1):
			if number % n == 0:
				return False
		return True
#7				
def perfect_check(number):
	'''Takes a positive integer and returns whether the number is 
	perfect. A perfect number is a number that equals the sum of proper 
	its proper factors. A proper factor is any factor except the number itself.'''
	factorList = 0
	for n in range(number,0):
		if factor_check(number, n) == True:
			factorList += n
	if factorList == number:
		return True
	else:
		return False
#8
def sum_even_check(number):
	'''Takes a positive integer as a parameter and returns true if
	the sum of the digits of the number divides evenly into 
	the number, false otherwise'''
	if number % sum_digit(number) == 0:
		return True
	else: 
		return False
		
	