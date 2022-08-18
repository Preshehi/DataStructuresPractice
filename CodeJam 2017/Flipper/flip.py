def flip(L,k):
	n=0
	res=[]
	while '-' in L:
		x=L.index('-')
		turn(L,x,k)
		if tuple(L) in res:
			n='IMPOSSIBLE'
			break
		else:
			res.append(tuple(L))
			n=n+1
	return n

def turn(L,x,k):
	if x<=len(L)-k:
		for y in range(x,x+k):
			if L[y]=='-':
				L[y]='+'
			else:
				L[y]='-'
	else:
		for y in range(x-len(L)+k,len(L)):
			if L[y]=='-':
				L[y]='+'
			else:
				L[y]='-'

small=open('small.in')
smallout=open('smallout.txt', 'w')
t=int(small.readline())
for r in range(1,t+1):
	M,K=small.readline().split(' ')
	k=int(K)
	L=[]
	for c in M:
		L.append(c)
	smallout.write(('Case #%s: %s\n' % (r, flip(L,k))))
