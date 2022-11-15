# Behavioral Pattern
# Notify everyone

# Observer pattern is used when there is one-to-many relationship between objects such as if one object is modified, its depenedent objects are to be notified automatically.

class GroupChat:
  def __init__(self):
    self.__observer = []
    
  def attach(self, observer):
    self.__observer.append(observer)
    
  def add_new_message(self,msg):
    self.notify(msg)
    
  def notify(self, msg):
    for observer in self.__observer:
      observer.update(msg)
      
      
class Observer:
  def __init__(self,name):
    self.name = name
    
  def update(self,msg):
    print(f"New Message for {self.name}: {msg}")   
    
    
messenger = GroupChat()
rakib = Observer('Rakib')
Tamim = Observer('Tamim')

messenger.attach(rakib)
messenger.attach(Tamim)

messenger.add_new_message("HEllo EveryOne")