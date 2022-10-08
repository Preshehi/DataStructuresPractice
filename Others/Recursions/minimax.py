def minimax(S,pointer=0):
	"""
	This function uses recursion to return the minimum and maximum of a
	passed sequence.
	It returns a list with two items, the first being the minimum and
	the second being the maximum
	"""
	if pointer==len(S)-1:
		return [S[pointer],S[pointer]]
	res=minimax(S,pointer+1)
	if S[pointer]<res[0]:
		res[0]=S[pointer]
	if S[pointer]>res[1]:
		res[1]=S[pointer]
	return res
