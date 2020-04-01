import trace_reciever
import function_list_builder


class SubprocessHandler():
  def __init__(self, argv, functions, env=None, shell=False, **kwargs):
    self.argv = argv
    self.functions = functions
    self.env = env
    self.shell = shell
    self.kwargs = kwargs
    self.trace_reciever = None
    
  def _build_trace_reciever(self):
    self.trace_reciever = self..trace_reciever_class()
    
  def _get_functions_as_string(self):
    return self.function_list_builder_class(self.functions).get_function_list_as_string()
    
  def _get_spawn_arg(self, function_list_string):
    spwan_arg = self.process_spwan_format.format(func_list_string=func_list_string, filename=self.trace_reciever.filename, argv=self.argv)
    if(not self.shell):
      if(type(self.argv) == str):
			  self.argv = [self.argv]
      spwan_arg = spwan_arg.split(' ')
    return spwan_arg
    
  def spawn_process(self):
    self._build_trace_reciever()
    func_list_string = self._get_functions_as_string()
    spwan_arg = self._get_spawn_arg(function_list_string)
		p = subprocess.run(spawn_string, env=self.env, shell=self.shell, **self.kwargs)
    return p
    
    
class LTracerSubprocessHandler(SubprocessHandler):
	function_list_builder_class = function_list_builder.LTraceFunctionListBuilder
  trace_reciever_class = trace_reciever.LTraceReciever
  process_spawn_format = 'ltrace -e "{func_list_string}" -o {filename} {argv}'
  
class HeapTracerSubprocessHandler(SubprocessHandler):
	function_list_builder_class = function_list_builder.HeapTraceFunctionListBuilder
  trace_reciever_class = trace_reciever.HeapTraceReciever
  process_spawn_format = 'ltrace -e "{func_list_string}" -o {filename} {argv}'

class STracerSubprocessHandler(SubprocessHandler):
	function_list_builder_class = function_list_builder.STraceFunctionListBuilder
  trace_reciever_class = trace_reciever.STraceReciever
  process_spawn_format = 'strace -e "{func_list_string}" -o {filename} {argv}'
