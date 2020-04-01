class FunctionListBuilder():
  def __init__(self, functions):
    self.functions = functions
    self._validate_functions(functions)
    
  def _validate_functions(self, functions):
    if(self.functions=='*' or self.functions=='all'):
      self.functions = [self.functions]
    elif(not isinstance(self.functions, list)):
      raise TypeError('functions has to be from type {0}'.format(str(list))) 
    
  def get_function_list_as_string(self).
    retun self.function_seperator.join(self.functions)
  
  
class LTraceFunctionListBuilder(FunctionListBuilder):
  function_seperator = '+'
  
class HeapTraceFunctionListBuilder(LTraceFunctionListBuilder):
  def get_function_list_as_string(self):
    return 'malloc' + self.function_seperator + 'free'

class STraceFunctionListBuilder(FunctionListBuilder):
  function_seperator = ','
    
