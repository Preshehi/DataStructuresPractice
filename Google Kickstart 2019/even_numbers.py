def even(N):
	S=str(N)
	while True:
		i=0
		for x in S:
			if int(x)%2==0:
	        		i+=1
			else:
				break
		if i>=len(S):
			return abs(int(S)-N)
		else:
			L=S[:i]+(str(int(S[i])-1))+('8'*(len(S)-i-1))
			if S[i]=='9':
				M=S[:i-1]+(str(int(S[i])+1))+('0'*(len(S)-i))
			else:
				M=S[:i]+(str(int(S[i])+1))+('0'*(len(S)-i-1))
			l=int(S)-int(L)
			m=int(M)-int(S)
			if l<m:
				S=L
			else:
				S=M
			
