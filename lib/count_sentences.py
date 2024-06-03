#!/usr/bin/env python3
import re 
class MyString:
  def __init__ (self,  value = ''):
      self.value = value
      
    
  
  @property
  def value(self):
    return self._value 

  @value.setter
  def value(self, value):
    if type(value) == str :
      self._value = value
    else:
      print ("The value must be a string.")
    




  def is_sentence(self):
    value = self.value 
    if value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    value = self.value
    if value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    value = self.value
    if value[-1] == '!':
        return True
    else:
        return False
    
  def count_sentences(self):
    value = self.value
    if not value:
      return 0
    
    total = re.split(r'[.!?]\s+', value)

    print('This is the length', (total))
    return len(total)
  
    
    
    