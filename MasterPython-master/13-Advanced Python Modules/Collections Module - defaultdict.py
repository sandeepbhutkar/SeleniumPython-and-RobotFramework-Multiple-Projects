# defaultdict is dictionary like object which provides all methods provided by dictionary
# using defaultdict is faster than doing the same using dict.set_default method

from collections import defaultdict
d = {'k1':1} # normal dictionary

print(d['k1']) # returns value 1
# lets try to display value of non-existing key

#print(d['k2']) # we get KeyError: 'k2'

# Lets define a defaultdict
df = defaultdict(lambda: 0)
print(df['k2']) # returns 0 for non-existing key 'k2'