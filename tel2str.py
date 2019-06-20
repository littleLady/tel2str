import itertools
# implemented using Python 2.7.16
# print all letter combinations of digits
def print_combination(digits):
	if not validate_digits(digits):
		print("invalid digits!")
		return
	dict = {
	0:[''],
	1:[''],
	2:['a','b','c'],
	3:['d','e','f'],
	4:['g','h','i'],
	5:['j','k','l'],
	6:['m','n','o'],
	7:['p','q','r','s'],
	8:['t','u','v'],
	9:['w','x','y','z']}
	if isinstance(digits, int):
		digits = [int(d) for d in str(digits)]
	temp = []
	for el in digits:
		temp.append(dict[el])
	result = list(itertools.product(*temp))
	for el in result:
		print(''.join(el)),
	print("")
		
# verify whether digits is valid or not
def validate_digits(digits):
	if isinstance(digits, (list,)) and validate_int_list(digits):
		return True
	elif isinstance(digits, int) and validate_int_range(digits):
		return True
	else:
		return False

# verify whether digits list is valid or not
def validate_int_list(digits):
	for i in digits:
		if not (isinstance(i, int) and (i >= 0 and i <= 9)):
			return False
	return True

# verify whether single digit is valid or not
def validate_int_range(s_digit):
	if s_digit >= 0  and s_digit <= 99:
		return True
	return False
		
# valid digits list
print("--------------result for valid digits list--------------")
print_combination([2,3])
print_combination([9])
print_combination([0])
print_combination([0,1,2,3,9])
print_combination([2,2])
# invalid digits list
print("--------------result for invalid digits list--------------")
print_combination([-1,2,3])
print_combination(['a',2,3])
# valid single digit
print("--------------result for valid single digit--------------")
print_combination(0)
print_combination(99)
# invalid single digit
print("--------------result for invalid single digit--------------")
print_combination(-1)
print_combination(100)
# invalid digit type
print("--------------result for invalid digit type--------------")
print_combination('a')
