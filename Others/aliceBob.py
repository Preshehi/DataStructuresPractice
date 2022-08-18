class InternetApplication():
	class User():
		def __init__(self,name):
			self._packet=0
			self._name=name

		def increase(self):
			self._packet+=1
			return

		def reduce(self):
			self._packet-=1
			return

	def __init__(self):
		self._users=0

	def _add_user(self,name):
		user=User(name)
		self._users+=1
		return

	def process(self,Alice,Bob):	
		while True:
			if Alice.packet>0:
				Alice.send()
				Bob.receive()
				Bob.read()
		return
