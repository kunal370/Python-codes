print('assigning multiple values to variables')
a,b,c=10,20,30
print('',a,'\n',b,'\n',c)
print('*****************************************************')
a=b=c='orange'

print(a)
print(b)
print(c)
print('*****************************************************')

a=b=c=90
print(a)
print(b)
print(c)
print('*****************************************************')

#print type
age=23
name='kunal'
height=175.6
com=2+3j
print(type(age))
print(type(name))
print(type(height))
print(type(com)) #<-- complex data type

print('*****************************************************')
#Type Casting
f1=5.6
print(f1)
a=int(f1) # conversion from float to int
print(a)
print('*****************************************************')

x=10
print(x)
y=float(x) # conversion from int to float

print(y)

z=str(y) #float to string
print(z)

print('*****************************************************')

price=59
print(f'price of product is {price:.4f}')#.4f--> refers to how many decimals we want 
