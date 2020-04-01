class TracePrinter():
  @staticmethod
  def print_trace(trace_calls_list):
    for trace_call in trace_calls_list:
      TracePrinter.print_trace_call(trace_call)
  
  @staticmethod
  def print_trace_call(trace_call):
	  print('\033[0;33m'+ '<trace> ' + '\033[0;96m' + trace_call.function_name + '(' + '\033[0;34m' + ','.join(trace_call.function_arguments) + '\033[0;96m' + ')' + '\033[0m' + ' = ' + '\033[0;95m' + trace_call.return_value  +'\033[0m')

    
class MallocedChunksPrinter():
  @staticmethod
  def print_malloced_chunks(malloced_chunks):
    for malloced_chunk in malloced_chunks:
      MallocedChunksPrinter.print_malloced_chunk(malloced_chunk)
   
  @statcimethod
  def print_malloced_chunk(malloced_chunk):
    print('\033[0;33m' + 'MALLOCED CHUNK: ' + '\033[0;96m' + 'address: ' + '\033[0;95m' + str(malloced_chunk.address) + '\033[0;96m' + ' size: ' + '\033[0;95m' + str(malloced_chunk.size) + '\033[0m')
  
class FreedChunksPrinter():  
  @staticmethod
  def print_freed_chunks(self, freed_chunks):
    for freed_chunk in freed_chunks:
      FreedChunksPrinter.print_malloced_chunk(freed_chunk)
  
  @statcimethod
  def print_malloced_chunk(freed_chunk):
    print('\033[0;33m' + 'FREED CHUNK: ' + '\033[0;96m' + 'address: ' + '\033[0;95m' + str(freed_chunk.address) + '\033[0m')
  
