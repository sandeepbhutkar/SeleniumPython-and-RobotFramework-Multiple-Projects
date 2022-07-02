name="Sand"
age=25
sal=1000.24

#Approch1
print(name,age,sal)
#Approch2
print("name is :", name)
print("age is :", age)
print("sal is :", sal)
#Approch3    #data type and %
print("Name is:%s Age is:%d Sal is:%g"%(name,age,sal))
#%s represent string , %d represent int, %g represent float
#Approch4  #.format curly bracket
print("Name{},Age{}.Sal{}".format(name,age,sal))
#Approch5
print("Name:{0}Age{1}Sal:{2}".format(name,age,sal))    #indexing