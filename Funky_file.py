from datetime import date
from datetime import time
def insert_integer_element(element):
    j = 0
    while j < 1:
        try:
            int(element)
        except ValueError:
            print('Wrong element type.')
            element = input('Insert new element ')
        else:
            j += 1
            element = int(element)
    return(element)
def insert_float_element(element):
    j = 0
    while j < 1:
        try:
            float(element)
        except ValueError:
            print('Wrong element type.')
            element = input('Insert new element ')
        else:
            j += 1
            element = float(element)
    return(element)
#def not_a_letter(element):
 #   j = 0
  #  i = int(0)
   # for i in element:
    #  if (element[i].isalpha() == 0):
     #   print("There is something that is not a letter. Enter a new word: ")
      #  continue
#      else:
 #       j = 1
  #  return j

def wrong_size(element, min, max):
    while ((element < min) or (element > max)):
        element = input('Incorrect value. Enter a new one: ')
        element = insert_integer_element(element)

m_w_31 = [1, 3, 5, 7, 8, 10, 12]
m_w_30 = [4, 6, 9, 11]

def read_journey_from_file(file, journey, NOJ, mylist):
    print("Reading journey number ", NOJ + 1)
    with open(file) as f:
        line = f.read().splitlines()

#        print("Checking city...")
#        j = 0
#        while j != 1:
#          j = not_a_letter(line[NOJ * 9 + 0])
#          line[NOJ * 9 + 0] = input("Enter a new city: ")
        setattr(journey, "city", line[NOJ * 9 + 0])
        
        print("Checking budget...")
        line[NOJ * 9 + 1] = float(line[NOJ * 9 + 1])
        while (line[NOJ * 9 + 1] > 500):
            line[NOJ * 9 + 1] = input("You are not that rich. Enter a new budget: ")
            line[NOJ * 9 + 1] = float(line[NOJ * 9 + 1])
        setattr(journey, "budget", line[NOJ * 9 + 1])
        
        print("Checking start year...")
        line[NOJ * 9 + 2] = insert_integer_element(line[NOJ * 9 + 2])
        wrong_size(line[NOJ * 9 + 2], 2020, 999999999)
        print("Checking start mounth...")
        line[NOJ * 9 + 3] = insert_integer_element(line[NOJ * 9 + 3])
        wrong_size(line[NOJ * 9 + 3], 1, 12)
        print("Checking start day...")
        line[NOJ * 9 + 4] = insert_integer_element(line[NOJ * 9 + 4])
        if (line[NOJ * 9 + 3] in m_w_31):
            wrong_size(line[NOJ * 9 + 4], 1, 31)
        if (line[NOJ * 9 + 3] in m_w_30):
            wrong_size(line[NOJ * 9 + 4], 1, 30)
        if (line[NOJ * 9 + 3] == 2):
            if (line[NOJ * 9 + 2] % 4 != 0):
                wrong_size(line[NOJ * 9 + 4], 1, 28)
            else:
                wrong_size(line[NOJ * 9 + 4], 1, 29)
        setattr(journey, "start_date", date(int(line[NOJ * 9 + 2]), int(line[NOJ * 9 + 3]), int(line[NOJ * 9 + 4])))
        
        print("Checking end year...")
        line[NOJ * 9 + 5] = insert_integer_element(line[NOJ * 9 + 5])
        wrong_size(line[NOJ * 9 + 5], 2020, 999999999)
        print("Checking end mounth...")
        line[NOJ * 9 + 6] = insert_integer_element(line[NOJ * 9 + 6])
        wrong_size(line[NOJ * 9 + 6], 1, 12)
        print("Checking end day...")
        line[NOJ * 9 + 7] = insert_integer_element(line[NOJ * 9 + 7])
        if (line[NOJ * 9 + 6] in m_w_31):
            wrong_size(line[NOJ * 9 + 7], 1, 31)
        if (line[NOJ * 9 + 6] in m_w_30):
            wrong_size(line[NOJ * 9 + 7], 1, 30)
        if (line[NOJ * 9 + 6] == 2):
            if (line[NOJ * 9 + 5] % 4 != 0):
                wrong_size(line[NOJ * 9 + 7], 1, 28)
            else:
                wrong_size(line[NOJ * 9 + 7], 1, 29)
        setattr(journey, "end_date", date(int(line[NOJ * 9 + 5]), int(line[NOJ * 9 + 6]), int(line[NOJ * 9 + 7])))
        
#        print("Checking username...")
#        j = 0
#        while j != 1:
#          j = not_a_letter(line[NOJ * 9 + 8])
#          line[NOJ * 9 + 8] = input("Enter a new username: ")
        setattr(journey, "username", line[NOJ * 9 + 8])
        mylist.append(journey)