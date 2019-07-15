num = int(input('Enter a value: '))
def is_even(num):
	if num % 2 == 0:
		print('Even')
		return True
	else:
		print('Odd')
		return False

print(is_even(num))
