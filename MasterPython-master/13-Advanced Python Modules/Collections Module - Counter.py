# The collections module is in-built module that implements specialized container datatypes providing
# alternatives to Python's builtin general purpose container
# Counters
from collections import Counter
# We have list of random numbers:
l = [1,2,3,5,6,3,3,6,7,8,2,1,1,1,3,3,3,4,5,5]
print(Counter(l)) # counter counts no. of objects in list

# Lets try it on string
s = 'sdhksjfguweaadsfassda'
print(Counter(s)) # counter counts no. of characters in string

# one more example
s = 'Lets count how many times each word appears in the sentence how many times show up up'

words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(3)) # this will return three most common words in the sentence

print(sum(c.values())) # returns total words in sentence