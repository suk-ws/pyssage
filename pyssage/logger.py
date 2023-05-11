from pyssage.appender import IAppender
from pyssage.components.restrictions import RestrictionToLog
from pyssage.log.log import Log, levels
from pyssage.log.message import Message


class Logger:
	
	def __init__(
			self,
			*appenders: IAppender,
	):
		
		self.appenders = list(appenders)
		self.restrictions: list[RestrictionToLog] = []
		
	
	def __push_to_all_appender (self, log: Log):
		for i in self.appenders:
			i.push_log(log)
	
	def log (self, log: Log):
		self.__push_to_all_appender(log)
	
	
	def trace(self, *msg: str):
		self.log(Log(Message(*msg), levels.TRACE))
	
	def debug(self, *msg: str):
		self.log(Log(Message(*msg), levels.DEBUG))
	
	def info(self, *msg: str):
		self.log(Log(Message(*msg), levels.INFO))
	
	def warning(self, *msg: str): self.warn(*msg)
	def warn(self, *msg: str):
		self.log(Log(Message(*msg), levels.WARN))
	
	def error(self, *msg: str):
		self.log(Log(Message(*msg), levels.ERROR))
	
	def fatal(self, *msg: str):
		self.log(Log(Message(*msg), levels.FATAL))
	
