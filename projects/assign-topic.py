import random
random.seed()

topics = {1:'file/directory permissions',
          2:'intrusion detection/prevention systems',
          3:'SQL injection prevention',
          4:'XSS prevention',
          5:'firewalls',
          6:'logging'}

available = [1,2,3,4,5,6]
num_groups = 6

for group in range(1,num_groups+1):
    choice_index = random.randint(0,len(available)-1)
    choice = available[choice_index]
    print("Group",group,"is assigned",topics[choice])
    print()
    available.remove(choice)
    input()
    
