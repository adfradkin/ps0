import ps0
#################################
################0################
print("F0 case 1: ")

if ps0.is_even(5) == True:
	print("The number is even. ")
else:
	print("The number is odd. ")
	
#################################	
print("F0 case 2: ")

if ps0.is_even(5) == True:
	print("The number is even. ")
else:
	print("The number is odd. ")
	
#################################
################1################
print("F1 case 1: ")

number1 = 256
print(ps0.digit_counter(number1))
#################################
print("F1 case 2: ")

number1 = 3758
print(ps0.digit_counter(number1))
#################################
###############2#################
print("F2 case 1: ")

number2 = 256
print(ps0.sum_digit(number2))
#################################
print("/nF2 case 2: ")

number2 = 3758
print(ps0.sum_digit(number2))
#################################
################3################
print("F3 case 1: ")

number3 = 47
print (ps0.add_below(number3))
#################################
print("F3 case 2: ")

number3 = 6
print(ps0.add_below(number3))

#################################
################4################
print("F4 case 1: ")

number4 = 6
print(ps0.factorial(number4))
#################################
print("F4 case 2: ")

number4 = 1
print(ps0.factorial(number4))

#################################
################5################
print("F5 case 1: ")

number5 = 10
factor5 = 1
if ps0.factor_check(number5, factor5) == True:
	print("The number is a factor")
else:
	print("The number is not a factor")
#################################
print("F5 case 2: ")

number5 = 13
factor5 = 5
if ps0.factor_check(number5, factor5) == True:
	print("The number is a factor")
else:
	print("The number is not a factor")
#################################
################6################
print("F6 case 1: ")

number6 = 10
if ps0.prime_check(number6) == True:
	print("The number is prime")
else:
	print("The number is not prime")
#################################
print("F6 case 2: ")

number6 = 47
if ps0.prime_check(number6) == True:
	print("The number is prime")
else:
	print("The number is not prime")
#################################
################7################
print("F7 case 1: ")

number7 = 10
if ps0.perfect_check(number7) == True:
	print("The number is perfect")
else:
	print("The number is not perfect")
#################################
print("F7 case 2: ")

number7 = 6
if ps0.perfect_check(number7) == True:
	print("The number is perfect")
else:
	print("The number is not perfect")

#################################
################8################
print("F8 case: 1")
number8 = 798
if ps0.sum_even_check(number8) == True:
	print("The sum of all the digits in the number divide equally into it.")
else:
		print("The sum of all the digits in the number dont' divide equally into it.")


#################################
print("F8 case:2")
number8 = 2
if ps0.sum_even_check(number8) == True:
	print("The sum of all the digits in the number divide equally into it.")
else:
		print("The sum of all the digits in the number dont' divide equally into it.")



























