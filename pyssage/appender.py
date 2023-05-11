from abc import ABC, abstractmethod
from pyssage.components.restrictions import RestrictionToLog
from pyssage.formatter import ILogFormatter

from pyssage.log.log import Log


class IAppender (ABC):
	
	@abstractmethod
	def push_log (self, log: Log) -> bool:
		pass
	

class Appender (IAppender):
	
	def __init__(self, formatter: ILogFormatter) -> None:
		
		super().__init__()
		self.formatter = formatter
		
		self.restrictoions_log: list[RestrictionToLog] = []
		
	
	def push_log(self, log: Log) -> bool:
		# apply Log restrictions
		for restriction in self.restrictoions_log:
			if not restriction.check(log):
				return False
		return True
		
	

class ConsoleAppender (Appender):
	
	def push_log(self, log: Log) -> bool:
		if not super().push_log(log): return False
		print(self.formatter.format(log))
		return True
		
	
