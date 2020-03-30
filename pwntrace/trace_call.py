class ValueConverter()
  def __init__(self, value):
    self.value = value
    
  def convert_value(self):
    try:
      return self._convert_value_to_int()
    except TypeError:
      return val
      
  def _convert_value_to_int(self):
    if(self.val.startswith(('0x', '\x'))):
      return int(self.val, 16)
    elif(self.val.startswith(('0o', '\')):
      return int(self.val, 8)
    else:
      return int(self.val, 10)



class TraceCall():
  def __init__(self, function_name, return_value, function_arguments):
    self.function_name = function_name
    self.return_value = return_value
    self.function_arguments = function_arguments
    
  @classmethod
  def from_line(cls, line):
    line = line.split('=')
    fc = line[0].strip()
    ret = ValueConverter(line[1].strip()).convert_value()
    fn = fc[:fc.rfind('(')]
    args = [ValueConverter(arg).convert_value() for arg in fc[fc.rfind('(')+1:fc.rfind(')')].split(',')]
    return cls(fn, ret, args)
    
    
class HeapChunk():
  def __init__(self, address, size):
    self.address = address
    self.size = size
    
  def equal_with_call(self, call):
    return bool(self.address == call.function_arguments[0])
    
  @classmethod
  def from_trace_call(cls, trace_call):
    return cls(trace_call.return_value, trace_call.function_arguments[0])
    
