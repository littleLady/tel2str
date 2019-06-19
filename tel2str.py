import itertools
def print_combination(list_int):
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
	temp = []
	for el in list_int:
		temp.append(dict[el])
	result = list(itertools.product(*temp))
	for el in result:
		print(''.join(el)),


list_int = [1,2,3,4]

print_combination(list_int)

