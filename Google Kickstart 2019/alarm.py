import sys



def CreateArray(N,x1,y1,C,D,E1,E2,F):

	A=['']*N
	x=['']*N
	y=['']*N 
	A2=[]

	x[0],y[0]=x1,y1
	A[0]=(x[0]+y[0])%F

	for i in range(1,N):

		x[i]=((C*x[i-1])+(D*y[i-1])+E1)%F

		y[i]=((D*x[i-1])+(C*y[i-1])+E2)%F

		A[i]=(x[i]+y[i])%F

	for j in range(1,len(A)+1):
 
		h=0

		while h+j<=len(A):
  
			A2.append(A[h:h+j])
     
			h+=1

	print (A2)
	return A2


def CheckPower(L,i):

	Power=0

	for M in L:
		n=1
		for x in M:

			Power=Power+(x*pow(n,i))

			n+=1

	return Power


file=open('test.txt','r')
t=int(file.readline())

for r in range(1,t+1):

	N,K,x1,y1,C,D,E1,E2,F=map(int,file.readline().split(' '))

	L=CreateArray(N,x1,y1,C,D,E1,E2,F)

	result=0

	for i in range(1,K+1):

		result+=CheckPower(L,i)

	print ('Case #%s: %s' % (r,result%1000000007))

	sys.stdout.flush()
