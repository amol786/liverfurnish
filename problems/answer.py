#answer 3.  to reversse  the string
string = "Me And You"
x = " ".join(string.split(" ")[::-1])
print(x)

#answer 4. for unique random number in list 
"""
used set for reaching minimum
time complexity
"""
import random 
def generateRandomlist(mylist,start=1,end=1000):
    
    for x in range(100000):
        tmp = random.randint(start,end)
        mylist.append(tmp)
    
    return list(set(mylist))
        


mylist = [1, 2, 3, 4, 5, 6, 7 ,8,9,10,11,23,13,142,34,56]

print(generateRandomlist(mylist,1,1000))