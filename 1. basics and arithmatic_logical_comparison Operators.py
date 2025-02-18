# basics 
print('hello')
# taking input from user
print('*****************************************************')

str1=str(input('enter your name: '))
print('name is: ',str1)
print('*****************************************************')

# adddition of two numbers
a=4
b=5
c=a+b
print(c)
print('*****************************************************')

# taking input from user
print('arithmetic operators')
num1=int(input('enter the 1st number : '))
num2=int(input('enter the 2nd number : '))
add= num1+num2
sub= num1-num2
mul= num1*num2
div= num1/num2
mod= num1%num2
exp1=num1**2
exp2=num2**2
print('addition is: ', add,'\nsubstraction is: ',sub,'\nmultiplication is: ',mul,'\ndivision is: ',div,'\nmod is: ',mod,'\nexponential/ square of 1st no. is: ',exp1, '\nexponential / square of 2nd no. is: ',exp2)

print('*****************************************************')
print('comparison operators')
print('1st and 2nd no are equal: ',num1==num2)
print('1st and 2nd no are not equal: ',num1!=num2)
print('1st no. is greater than or equals to 2nd no.: ',num1>=num2)
print('1st no. is less than or equals to 2nd no.: ',num1<=num2)
print('1st no. is greater than 2nd no.: ',num1>num2)
print('1st no. is less than 2nd no.: ',num1<num2)


print('*****************************************************')
print('logical operators')
print('AND')
print(num1>num2 and num1!=num2) # it will only give true if both the conditions are true otherwise it will give false
print("OR")
print(num1>num2 or num1!=num2)# it will only give true if one of the  condition is true otherwise it will give false
print(num1==num2 or num1<=num2)
print(num1>=num2 or num1!=num2)
print(num1>num2 or num1==num2)
print('NOT')
n1=False
n2=True
print(not n1,'\n', not n2) #If given condition is true  → change to false or vise varsa


print('*****************************************************')


print('Accept the basic salary of emp from user \nCalculate the gross based on following criteria \nCalculate the gross salary of emp & display the output')
'''
Cal HRA 40% of basic
Cal  DA  20% of basic
Cal PF 12 % of basic
Use PT =200
gross= (bs+hra+da) -(pf+pt)
Bs = 
Hra -
Da - 
Pf -
Pt -200
Gross -
'''
basic=float(input('enter the basic salary: '))
HRA=basic*40//100
DA=basic*20//100
PF=basic*12//100
PT=200
Gross=(basic+HRA+DA)-(PF+PT)
print('Gross salary is : ',Gross,'₹')
print('*****************************************************')
