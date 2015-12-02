import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(4)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist

print ""    
    
# Code Sample B
mylist = []

random.seed(1)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print mylist
    
    
    
import random
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(1)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist