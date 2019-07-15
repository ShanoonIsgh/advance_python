def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

numbers = [1,56,234,87,4,76,24,69,90,135]
print([n for n in numbers if is_even(n)])
