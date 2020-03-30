import os
import string
import radnom


class TraceReciever():
  def __init__(self, fifo_name):
    self.fifo_name = fifo_name
    self.seek_pointer = 0
    self._create_fifo()
    
  def _create_fifo(self):
    if(not os.path.exists(self.fifo_name)):
      os.mkfifo(self.fifo_name)
    
  def get_latest_fifo_output(self):
    try:
      return self._get_latest_fifo_output()
    except EOFError:
      return ''
    
  def _get_latest_fifo_output(self):
    with open(self.fifo_name, 'r') as f:
      f.seek(self.seek_pointer)
      out = f.read()
      if('\n' in out):
        last_newline = out[::-1].rfind('\n')
        self.seek_pointer += last_newline+1
        return out[:last_newline+1]
      return ''
  
  @classmethod
  def create_reciever(cls):
    rand_str = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
	  fifo_name = cls.fifo_name_prefix + rand_str
	  return cls(fifo_name)
    

class LTraceReciever(TraceReciever):
  fifo_name_prefix = "/tmp/ltrace-fifo-"
  

class HeapTraceReciever(TraceReciever):
  fifo_name_prefix = "/tmp/heap_trace-fifo-"
  
 
class STraceReciever(TraceReciever):
  fifo_name_prefix = "/tmp/strace-fifo-" 
