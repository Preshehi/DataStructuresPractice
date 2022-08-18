def tidy(N):
	g=''
	y=list(str(N))
	z=y[:]
	z.sort()
	while not z==y:
		n=0
		while True:
			if z[n]==y[n]:
				n=n+1
				continue
			else:
				c=''
				y=y[:n+1]+['0' for x in range(len(z)-n-1)]
				for i in y:
					c=c+i
				j=int(c)-1
				y=list(str(j))
				z=y[:]
				z.sort()
				break
	for m in y:
		g=g+m
	return int(g)

large=open('large.in')
largeout=open('largeout.txt', 'w')
t=int(large.readline())
for r in range(1,t+1):
	N=int(large.readline())
	largeout.write('Case #%s: %s\n' % (r,tidy(N)))
