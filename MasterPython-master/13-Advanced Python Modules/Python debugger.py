#Interactive debugger helps interactively debug issue
import pdb

x = [1,2,3]
y = 2
z = 3

pdb.set_trace() # SET THE TRACE where the error occured
print(x + y)