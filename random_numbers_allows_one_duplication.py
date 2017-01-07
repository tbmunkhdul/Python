# fun(5) -> 4,3,2,1,1
# fun allow only one duplication, unsorted
import random

def fun(n):
    mylist = [i for i in range(1, n + 1)]
    random.shuffle(mylist)
    duplicate_value = random.randint(1, n)
    index = None
    while True:
        index = random.randint(0, n - 1) 
        if mylist[index] != duplicate_value:         
            mylist[index] = duplicate_value
            break
    return mylist

print (fun(10))

print ("Ends")

# version 2
def generateSQ(num):
    ls = [i for i in range(num)]
    random.shuffle(ls)
    dupval = random.choice(ls)
    randomindex = random.choice(ls)
    while True:
        if ls.index(dupval) != randomindex:
            ls[randomindex] = dupval
            break
    return '{}'.format(ls)


mygenlist = generateSQ(10)
print(mygenlist)