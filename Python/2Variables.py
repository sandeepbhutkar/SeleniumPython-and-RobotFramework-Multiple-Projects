a=5
print(type(a))
b=4.4
print(type(b))
c=10j
print(type(c))
d='Sandeep'
print(type(d))
e=True
print(type(e))

a,b,c=5,4.4,"Sandeep"
print(a,b,c)

a=b=c='Hello'
print(a,b,c)

#exchange/exchange x and y value
x=2
y=3
x,y=y,x
print(x)
print(y)

#redeclare of var
a=10
print("before",a)
a=100
print("after",a)

#Deleting Var
a=10
print(a)
del a
print(a)