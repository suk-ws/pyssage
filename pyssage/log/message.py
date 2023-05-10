
class Message:
	
	def __init__(self, message: str|list[str]):
		
		self.message: list[str]
		
		if isinstance(message, str):
			self.message = message.split("\n")
		else:
			self.message = message
		
	
