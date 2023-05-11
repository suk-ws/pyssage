from threading import Thread, current_thread
import time

from pyssage.log.message import Message


class LogLevel:
	
	def __init__(self, level: float, tag: str):
		
		self.level: float = level
		self.tag: str = tag
		
	
	def __str__(self) -> str:
		return self.__repr__()
	
	def __repr__(self) -> str:
		return f"<{self.tag}({self.level})>"
	
	def __eq__(self, __value: object) -> bool:
		return isinstance(__value, LogLevel) and self.level == __value.level
	
	def __gt__(self, __value: object) -> bool:
		return isinstance(__value, LogLevel) and self.level > __value.level
	
	def __lt__(self, __value: object) -> bool:
		return isinstance(__value, LogLevel) and self.level < __value.level
	
	def __ge__(self, __value: object) -> bool:
		return isinstance(__value, LogLevel) and self.level >= __value.level
	
	def __le__(self, __value: object) -> bool:
		return isinstance(__value, LogLevel) and self.level <= __value.level
	

class levels:
	ALL   = LogLevel(-float('inf'), "####")
	TRACE = LogLevel(-1.0,          "TRAC")
	DEBUG = LogLevel(-0.1,          "DBUG")
	INFO  = LogLevel( 0.0,          "INFO")
	WARN  = LogLevel( 0.5,          "WARN")
	ERROR = LogLevel( 1.0,          "EROR")
	FATAL = LogLevel(10.0,          "FTAL")
	NONE  = LogLevel(float('inf'),  "!!!!")


class Log:
	
	def __init__(self, message: Message, level: LogLevel, thread: Thread|None = None, timestamp: float|None = None):
		
		self.message: Message = message
		self.level: LogLevel = level
		self.thread: Thread = thread if (thread is not None) else current_thread()
		self.timestamp: float = timestamp if (timestamp is not None) else time.time()
		
	
