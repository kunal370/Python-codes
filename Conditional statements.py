#Conditional statements in Python
print('IF')
age=int(input('Enter age: '))
if age>=18:
    print('you can vote')
print('*****************************************************')

print('IF.....ELSE')
if age>=18:
    print('you can vote')
else:
    print('you can not vote')
    
print('*****************************************************')
print('IF.....ELIF.....ELSE')
print('to check no is positive negative or zero')
num=int(input('number please:'))
if num>0:
    print('num is positive')
elif num<0:
    print('num is negative')
else:
    print('num is zero')
    
print('*****************************************************')
print('Homework')

print('Accept the 5 subject marks of student, calculate total  & percentage')

#        Per > 75    ‘ Grade A+’
#     Per > 60  and per<=75   ‘Grade A’
#  Per >=40  and per <=60   ‘Grade B’
# Per < 40   → ‘Fail’
eng=float(input('enetr the ENGLISH marks out of 100 : '))
maths=float(input('enetr the MATHS marks out of 100 : '))
hindi=float(input('enetr the HINDI marks out of 100 : '))
hist=float(input('enetr the HISTORY marks out of 100 : '))
sci=float(input('enetr the SCIENCE marks out of 100 : '))
total=eng+maths+hindi+hist+sci
print('total marks are: ',total)
per=total/500*100

print('percentage are : ',per)
if per>75:
    print('Grade A+')
if per>60 and  per<=75:
    print('Grade A')
if per>=40  and per<=60:
    print('Grade B')
if per<40:
    print('fail')
    
print('*****************************************************')

print('WAP to accept the year from user & check year is leap year or not')
yr=int(input('enre the year'))
if yr%4==0:
    print(yr,'is leap year')
else:
    print(yr,'is not leap year')

print('*****************************************************')
print('WAP to accept a number from user & print the last digit')
num1=int(input('enter the number: '))
last=num1%10
print('last digit is: ',last)

print('*****************************************************')
print('WAP to check entered number is divisible by 5 or not')
num2=int(input('enter the number: '))
if num2%5==0:
    print(num2,'is divisible by 5')
else:     
   print(num2,'is not divisible by 5')
   
print('*****************************************************')
   
print('Accept the bike price from user & add road tax as follows')
#      Price > 80000   15 % TAX
#      Price > 40000 & <80000  10% TAX
#      Else                       5% TAX


price=float(input('enter the price of bike: '))
if price>=80000:
    tax=price*15/100
    print(tax,'is your tax\n',tax+price,'is your total')
elif price>40000 and price<80000:
    tax=price*10/100
    print(tax,'is your tax\n',tax+price,'is your total')
else:
      tax=price*5/100
      print(tax,'is your tax\n',tax+price,'is your total')
      
print('*********************************************************')
print('# Accept value for variable a & b , and interchange the value ')
#        a=10
#        b=20
#  Output
#    a=20
#   b=10
c=0
a=int(input('enter the value of A: '))
b=int(input('enter the value of B: '))
# c=b
# b=a
# a=c
a,b=b,a
print('value of A : ',a,'\nvalue of B : ',b)
print('*********************************************************')
