import trace_reciever
import trace_call
import trace_printer
import trace_utils


class TraceCallGenerator():
  def __init__(self, trace_output):
    self.trace_output = trace_output.split('\n')
    
  def generate_calls(self):
    for line in filter(lambda x:("=" in x), self.trace_output):
      yield trace_call.TraceCall.from_line(line)
      
    
class TraceOutputLineParser().
  def __init__(self, trace_line):
    self.trace_line = trace_line
    self.trace_calls_list = list()
    
  def create_trace_calls(self):
    for line in self._generate_filtered_lines():
      self._trace_calls_list.append(TraceCall.from_line(line))
    return self.trace_calls_list
    
  def _generate_filtered_lines(self):
    lines = self.trace_output.split('\n'):
    for line in filter(lambda x:("=" in x), lines):
      yield line

class TraceCallsParser():
  def __init__(self):
    self.trace_calls = list()
    self.freed_chunks = list()
    self.malloced_chunks = list()
    
  def parse_trace_output(sef, trace_output):
    for call in TraceCallGenerator(trace_output).generate_calls():
      self._parse_call(call)
   
  def _parse_call(self, call):
    if("malloc" in call.function_name):
      self._parse_malloc(call)
    elif("free" in call.function_name):
      self._parse_free(call)
    self.trace_calls.append(call)
    
  def _parse_malloc(self, call):
	  if(call.return_value in self.freed_chunks):
		  self.freed_chunks.remove(call.return_value)
		self.malloced_chunks.append(trace_call.HeapChunk.from_call(call))
    
  def _parse_free(self, call):
    for chunk in self.malloced_chunks:
      if(chunk.equal_with_call(call)):
        self.malloced_chunks.remove(chunk)
        self.freed_chunks.append(chunk.address)
        break

    
    
  
    
 class Tracer():
  def __init__(self, trace_reciever, trace_calls_parser=None):
    if(not issubclass(trace_reciever, trace_reciever.TraceReciever)):
      raise TypeError('trace_reciever has to a subclass from {0}'.format(str(trace_reciever.TraceReciever)))
    self.trace_reciever = trace_reciever
    self.trace_calls_parser = (trace_calls_parser if(isinstance(trace_calls_parser, TraceCallsParser)) else TraceParser())
    
  def print_trace(self):
    trace_printer.TracePrinter().print_trace(self.trace_calls_parser.trace_calls)
    
  def parse_new_trace_calls(self):
    latest_trace_output = self.trace_reciever.get_latest_fifo_output()
    self.trace_calls_parser.parse_trace_output(latest_trace_output)
    
