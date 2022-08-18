class River():
	def __init__(self,args*):
		L=[]
		for x in args:
			L.append(x)
		self._river=L

	def move(