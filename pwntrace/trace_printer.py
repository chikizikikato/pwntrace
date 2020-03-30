class TracePrinter()
  def __init__(self):
    pass
  
  def print_trace(self, trace_calls_list):
    for trace_call in trace_calls_list:
      self.print_trace_call(trace_call)
  
  def print_trace_call(self, trace_call):
	  print('\033[0;33m'+ '<trace> ' + '\033[0;96m' + trace_call.function_name + '(' + '\033[0;34m' + ','.join(trace_call.function_arguments) + '\033[0;96m' + ')' + '\033[0m' + ' = ' + '\033[0;95m' + trace_call.return_value  +'\033[0m')
