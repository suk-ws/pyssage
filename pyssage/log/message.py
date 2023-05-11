
class Message:
	
	def __init__(self, *message: str):
		
		self.message: tuple[str]
		
		if message.__len__() == 0:
			raise RuntimeError("message cannot be empty.")
		elif message.__len__() == 1:
			self.message = tuple(message[0].split("\n"))
		else:
			self.message = message
		
	# def __str__(self):
	
