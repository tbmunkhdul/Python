# list comprehension is nice and fast and easy to use,
# but sometimes tradional for loop way is better
def list_comprehension(lst):
    list1 = [i for i in lst if i % 2 == 0]
    list2 = [i for i in lst if i % 3 == 0]
    list3 = [i for i in lst if i % 5 == 0]

def for_loop(lst):
    list1 = []
    list2 = []
    list3 = []
    for i in lst:
        if i % 2 == 0:
            list1.append(i)
        elif i % 3 == 0:
            list2.append(i)
        elif i % 5 == 0:
            list3.append(i)
        else:
            pass 

import cProfile
mylst = [i for i in range(100000)]
cProfile.run('list_comprehension(mylst)')
cProfile.run('for_loop(mylst)')
