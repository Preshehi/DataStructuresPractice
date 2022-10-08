def logarithm(n):
	"""
	This function returns the integer part of the base two 
	logarithm of any number, using recursion.
	i.e. It is the floor of the base two of any number.
	"""
	if n<2:
		return 0
	return logarithm(n//2)+1
