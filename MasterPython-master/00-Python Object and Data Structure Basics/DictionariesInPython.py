# Dictionaries are unordered mappings for storing objects
# Dictionary uses key-value pair for storing objects
# this key-value pair enables user to grab object withot its index
# {'key1':'value1','key2':'value2','key3':'value3'}

my_dict = {'key1':'value1','key2':'value2','key3':'value3'}
print(my_dict['key1']) # grab the value by key

# one more example
prices_lookup= {'apple':8.23,'grapes':11.8,'milk':2.12}
print(prices_lookup['grapes'])

# dictionary can hold various object types like list, dictionry within dictionary
d = {'k1':34,'k2':[2,4,5],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey'])

# Adding a key-value pair to an existing dictionary
d = {'k1':100, 'k2':200}
d['k3'] = 300
print(d)

#Over-writing a key-value
d['k1'] = 150
print(d)

# get all keys
print(d.keys())

#get all values
print(d.values())

#get itms as tuple
print(d.items())