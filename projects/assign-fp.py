import random
random.seed()

numStudents = 19
numGroups = 6
numReviewed = 2

reviewList=[]

#Create numStudents group numbers spread out evenly over list
for student in range(1,numStudents+1):

    test1=random.randint(1,numGroups)
    test2=random.randint(1,numGroups)
    while test2 == test1: #make sure they are different
        test2=random.randint(1,numGroups)
    print(test1,test2)
    reviewList.append(test1)
    reviewList.append(test2)

print()
for i in range(1,numGroups+1):
    print(i,reviewList.count(i))
    
##
##topics = {1:'file/directory permissions',
##          2:'intrusion detection/prevention systems',
##          3:'SQL injection prevention',
##          4:'XSS prevention',
##          5:'firewalls',
##          6:'logging'}
##
##available = [1,2,3,4,5,6]
##num_groups = 6
##
##for group in range(1,num_groups+1):
##    choice_index = random.randint(0,len(available)-1)
##    choice = available[choice_index]
##    print("Group",group,"is assigned",topics[choice])
##    print()
##    available.remove(choice)
##    input()
    
