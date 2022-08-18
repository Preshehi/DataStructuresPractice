def stall(M,k):
	for i in range(0,k):
		res=[]
		res1=[]
		res2=[]
		res4=[]
		for x in range(0,len(M)):
			if M[x]=='O':
				continue
			else:
				L=M[find(M,x,1):x].count('.')
				R=M[x+1:find(M,x,2)].count('.')
				res.append(min(L,R))
				res1.append(max(L,R))
				res2.append(x)
		y=max(res)
		if res.count(y)==1:
			z=res.index(y)
			occupy(M,res2[z])
		else:
			res3=[]
			for s in res:
				if s==max(res):
					res3.append(res1[res.index(s)])
			z=res1.index(max(res3))
			occupy(M,res2[z])
	return (res1[z],res[z])

def find(M,x,y):
	if y==2:
		for j in range(x,len(M)):
			if M[j]=='O':
				return j
	else:
		for j in range(x,-1,-1):
			if M[j]=='O':
				return j

def occupy(L,x):
	L[x]='O'

smallin=open('small2.in')
smallout=open('smallout2.txt','w')
t=int(smallin.readline())
for r in range(1,t+1):
	N,k=[int(x) for x in smallin.readline().split(' ')]
	L=['O']+['.' for j in range(0,N)]+['O']
	x,y=stall(L,k)
	smallout.write('Case #%s: %s %s\n' % (r,x,y))
