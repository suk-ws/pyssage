from abc import ABC, abstractmethod

from pyssage.log.log import Log, LogLevel, levels


class RestrictionToLog(ABC):
	
	@abstractmethod
	def check(self, log: Log) -> bool:
		pass
	

class LevelRestriction(RestrictionToLog):
	
	def __init__(
			self,
			min_level: LogLevel = levels.ALL,
			max_level: LogLevel = levels.NONE
	):
		
		self.min_level = min_level
		self.max_level = max_level
		
	
	def check(self, log: Log) -> bool:
		
		return log.level >= self.min_level and log.level <= self.max_level
		
	
