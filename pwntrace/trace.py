import subprocess_handler
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
    fake_freed_chunk = trace_call.FreedHeapChunk.from_trace_call(calll)
    if(fake_freed_chunk in self.freed_chunks):
      self.freed_chunks.remove(fake_freed_chunk)
    self.malloced_chunks.append(trace_call.MallocedHeapChunk.from_call(call))

  def _parse_free(self, call):
    for malloced_chunk in self.malloced_chunks:
      if(malloced_chunk.equal_with_call(call)):
        self.malloced_chunks.remove(malloced_chunk)
        self.freed_chunks.append(trace_call.FreedHeapChunk.from_malloced_chunk(malloed_chunk))
        break

   
 

 class Tracer():
  def __init__(self, subprocess_handler, trace_calls_parser=None):
    self.subprocess_handler = subprocess_handler
    self.trace_calls_parser = (trace_calls_parser if(isinstance(trace_calls_parser, TraceCallsParser)) else TraceCallsParser())

  def print_trace(self):
    trace_printer.TracePrinter.print_trace(self.trace_calls_parser.trace_calls)

  def parse_new_trace_calls(self):
    latest_trace_output = self.subprocess_handler.trace_reciever.get_latest_trace_output()
    self.trace_calls_parser.parse_trace_output(latest_trace_output)

  @classmethod
  def bind_tracer_to_process(cls, argv, functions, env=None, shell=False, **kwargs):
    subprocess_handler = cls.subprocess_handler_class(argv, functions, env=env, shell=shell, kwargs)
    return cls(subprocess_handler)
   

   
class LTracer(Tracer):
  subprocess_handler_class = subprocess_handler.LTraceSubprocessHandler
  
class HeapTracer(Tracer):
  subprocess_handler_class = subprocess_handler.HeapTraceSubprocessHandler

  def print_malloced_chunks(self):
    trace_printer.MallocedChunksPrinter.print_malloced_chunks(self.trace_calls_parser.malloced_chunks)

  def print_freed_chunks(self):
    trace_printer.FreedChunksPrinter.print_freed_chunks(self.trace_calls_parser.freed_chunks)

class STracer(Tracer):
  subprocess_handler_class = subprocess_handler.STraceSubprocessHandler'
