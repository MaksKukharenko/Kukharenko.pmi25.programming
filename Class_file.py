from datetime import date
from datetime import time

class JOURNEY:
  def __init__(self):
    self.city = "A"
    self.budget = 0.0
    self.start_date = date(1,1,1)
    self.end_date = date(1,1,1)
    self.username = "A"
  def __init__(self, city, budget, start_date, end_date, username):
    self.city = city
    self.budget = budget
    self.start_date = start_date
    self.end_date = end_date
    self.username = username
  def __str__(self):
    return f'{self.city}, {self.budget}, {self.start_date}, {self.end_date}, {self.username}'
  def __getitem__(self, key):
     return getattr(self, key)
  def __setitem__(self, key, value):
     setattr(self, key, value)

#setattr(Firstjourney, "ticket_price", 95)     #this works but i don't need this
#print(Firstjourney["ID"])                     #neither do i need this

