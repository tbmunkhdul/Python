old = {'a':33, 'b':44, 'c':55}
new = {'a':333, 'b': 444}
# expected_result = {'a':{'old':33, 'new':333}, 'b':{'old':44, 'new': 444}, 'c':{'old':55, 'new':None}}

res1 = {}
for oldkey, oldvalue in old.items():
    res1[oldkey] = {'old':oldvalue, 'new':new.get(oldkey, None)}

print(res1)
print("---------------------")
# expected_result = {'a':{'old':33, 'new':333}, 'b':{'old':44, 'new': 444}, 'c':None}
res2 = {}
for oldkey, oldvalue in old.items():
    if oldkey not in new:
        res2[oldkey] = None
        continue
    res2[oldkey] = {'old':oldvalue, 'new':new[oldkey]}
print(res2)
