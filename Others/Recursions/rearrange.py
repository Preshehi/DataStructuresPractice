def arrange(s,n,f=True):
	if n==len(s): return
	elif f and n>=0: arrange(s,n-1,f)
	f=False
	arrange(s,n+1,f)
	if s[n]%2==0 and n != 0: s[n],s[n-1]=s[n-1],s[n]
	return s
