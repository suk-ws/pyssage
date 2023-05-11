from abc import ABC, abstractmethod

from pyssage.log.log import Log


class ILogFormatter (ABC):
	
	@abstractmethod
	def format(self, log: Log) -> str:
		pass
	

class SimpleFormatter (ILogFormatter):
	
	def __init__(
			self,
			startof_timestamp : str = '[',
			endof_timestamp   : str = "]",
			startof_threadname: str = '[',
			endof_threadname  : str = ']',
			startof_leveltag  : str = '[',
			endof_leveltag    : str = ']',
			prompt_filter     : str = '\''
	):
		self.startof_timestamp  = startof_timestamp
		self.endof_timestamp    = endof_timestamp
		self.startof_threadname = startof_threadname
		self.endof_threadname   = endof_threadname
		self.startof_leveltag   = startof_leveltag
		self.endof_leveltag     = endof_leveltag
		self.prompt_filter      = prompt_filter
	
	def format(self, log: Log) -> str:
		
		formatted: str = ""
		prompt_first_line: str = (
			f"{self.startof_timestamp}{log.timestamp}{self.endof_timestamp}"
			f"{self.startof_threadname}{log.thread.name}{self.endof_threadname}"
		)
		prompt_next_lines: str = self.prompt_filter * prompt_first_line.__len__()
		prompt_public: str = f"{self.startof_leveltag}{log.level.tag}{self.endof_leveltag}"
		
		if (log.message.message.__len__() > 0):
			formatted += prompt_first_line + prompt_public + log.message.message[0]
		for i in range(1, log.message.message.__len__()):
			formatted += "\n"
			formatted += prompt_next_lines + prompt_public + log.message.message[i]
		
		return formatted;
		
	
