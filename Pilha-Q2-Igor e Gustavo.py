class Stack:
  def __init__(self):
    self.lista=[]
    self.tem = 0
  
  def push(self, valor):
    for i in range(len(self.lista)):
      if valor==self.lista[i]:
        self.tem = 1
    if self.tem==0:
      self.lista.append(valor)
    self.tem = 0

  
  def pop(self):
    if(not(self.isEmpty())):
      return self.lista.pop()
  
  def isEmpty(self):
    return(len(self.lista))==0

  def length(self):
    return(len(self.lista))

  
  def peek(self):
    if(not(self.isEmpty())):
      return self.lista[-1]

Stack = Stack()
Stack.push(2)
Stack.push(19)
Stack.push(2)
Stack.push(30)
Stack.push(25)
print (Stack.lista)
