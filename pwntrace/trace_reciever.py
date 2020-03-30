import tempfile

class TraceReciever():
  def __init__(self, tempfile):
    self.tempfile = tempfile    
    
  def get_latest_trace_output(self):
    try:
      return self.tempfile.read().decode('utf-8')
    except EOFError:
      return ''
  
  @classmethod
  def create_reciever(cls):
    return cls(tempfile.TemporaryFile(prefix=cls.filename_prefix))
    

class LTraceReciever(TraceReciever):
  filename_prefix = "/tmp/ltrace-"
  

class HeapTraceReciever(TraceReciever):
  filename_prefix = "/tmp/heap_trace-"
  
 
class STraceReciever(TraceReciever):
  filename_prefix = "/tmp/strace-" 
