poly= input('Write a polynomial of any degree')

def poly_derivative(poly):
	derv=num1=num2=''
	flag=False
	for _ in poly:
		if _.isdigit():
			if flag:
				num2+=_
			else:
				num1+=_
		elif _ in ('+','-'):
			if num2!='':
				temp=int(num1)*int(num2)
			else:
				temp=int(num1)
			if num2=='2':
				expo=var
			elif num2=='':
				expo=''
			else:
				expo=var+str(int(num2)-1)
			if temp>0:
				derv+='+'+str(temp)+expo
			else:
				derv+=str(temp)+expo
			flag=False
			num1=_
			num2=''
		elif _.isalpha():
			var=_
			flag=True
	if derv[0] in ('+','-'):
		return derv[1:]
	return derv

print (poly_derivative(poly))