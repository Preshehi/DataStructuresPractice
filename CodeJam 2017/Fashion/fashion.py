def stylepoints(L):
	n=0
	for M in L:
		for x in M:
			if x=='+' or x=='x':
				n=n+1
			elif x=='o':
				n=n+2
	return n

def get(L,i,j):
	row=[]
	col=[]
	for x in range(len(L)):
		row.append(L[i][x])
		col.append(L[x][j])
	return row,col

def diag(L,i,j):
	dia=[]
	for x in range(0,len(L)):
		for y in range(0,len(L)):
			if (i+j)==(x+y) or (i-j)==(x-y):
				dia.append(L[x][y])
	return dia

def check(L,x):
	res=[]
	for i in range(0,len(L)):
		for j in L[i+1:]:
			if x==1:
				if '+' in (L[i],j):
					continue
				elif '.' in (L[i],j):
					continue
				else:
					res.append('false')
			elif x==2:
				if 'x' in (L[i],j):
					continue
				elif '.' in (L[i],j):
					continue
				else:
					res.append('false')
	if 'false' in res:
		return 'false'
	else:
		return 'true'

def show(L):
	res=[]
	M=['o','x','+']
	g=stylepoints(L)
	for i in range(0,len(L)):
		for j in range(0,len(L)):
			y=L[i][j]
			for x in M:
				if x==y:
					continue
				else:
					L[i][j]=x
					m,n=get(L,i,j)
					a,b,c=(check(m,1),check(n,1),check(diag(L,i,j),2))
					if not 'false' in (a,b,c) and stylepoints(L)>g:
						res.append((x,i,j))
						g=stylepoints(L)
						break
					else:
						L[i][j]=y
						continue
	return res

x,y=[int(c) for c in input('\n').split(' ')]
L=[]
for j in range(0,x):
	res=['.' for i in range(0,x)]
	L.append(res)
for u in range(0,y):
	m,n,q=[s for s in input('\n').split(' ')]
	L[int(n)-1][int(q)-1]=m
f=show(L)
print (f)
