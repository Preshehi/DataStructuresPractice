import math
def recur_pali(c,n=0):
	if n==math.ceil((len(c)-1)/2):
		return c[n]==c[-n-1]
	return recur_pali(c,n+1) and (c[n]==c[-n-1])
