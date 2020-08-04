class Phone(object):
  number = ""
    
  def __init__(self, phone_number):
    self.number = "".join(list(filter(lambda x: x.isdigit(), phone_number)))
    if 10 > len(self.number) > 11:
      raise ValueError("Kys")
    elif len(self.number) == 11:
      if self.number[0] != "1":
        raise ValueError("1")
      else:
        del self.number[0]
        
    if self.number[0] not in str(range (2, 10)) and self.number[3] not in str(range (2, 10)):
      raise ValueError ("2")
      
      
  def pretty(self):
    p_n="("+self.number[0:3]+") "+self.number[3:6]+"-"+self.number[6:]
    return self.p_n