# An OrederedDict is a dictionary subclass that remembers the order in which its contents are added
# Lets first define normal dictionary
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


# out put of below is not necessarily will be ordered
for k,v in d.items():
    print(k,v)
# Now lets import OrderedDict
from collections import OrderedDict
d = OrderedDict()
print("OrderedDict output will be ordered: ")
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print(k,v)