# match case in  python
print('When you are writing any code for menu driven application')
'''
Example 1:
1. Eng
2. Hindi
3. Marathi

1. Prepaid
2. Postpaid

1. Bal
2. Plans
#to talk to customer care executive
'''

print('1. english')
print('2. Hindi')
print('3. marathi')
option=int(input("select one option from 1-3: "))
match option:
    case 1:
        print('you have selected english')
        print('select plan --> prepaid or postpaid')
        print('1. prepaid')
        print('2. postpaid')
        subop=int(input('select plan accordingly: '))
        match subop:
            case 1:
                print('you have selected prepaid')
                print('select balance or plan')
                print('1. balance')
                print('2. plan')
                sub1=int(input('select balance or plan: '))
                match sub1:
                    case 1:
                        print('you have sleceted balance ')
                        print('yoour balance is 0.00₹')
                    case 2:
                        print('you have sleceted plan ')
                        print('you have no plan')
                    case default:
                        print('you have selected wrong option')
            case 2:
                print('you have selected postpaid')
                print('select balance or plan')
                print('1. balance')
                print('2. plan')
                sub1=int(input('select balance or plan: '))
                match sub1:
                    case 1:
                        print('you have sleceted balance ')
                        print('yoour balance is 0.00₹')
                    case 2:
                        print('you have sleceted plan ')
                        print('you have no plan')
                    case default:
                        print('you have selected wrong option')
            case default:
                print('you have selected wrong option')
                
    case 2:
          print('you have selected Hindi')
          print('select plan --> prepaid or postpaid')
          print('1. prepaid')
          print('2. postpaid')
          subop=int(input('select plan accordingly: '))
          match subop:
              case 1:
                  print('you have selected prepaid')
                  print('select balance or plan')
                  print('1. balance')
                  print('2. plan')
                  sub1=int(input('select balance or plan: '))
                  match sub1:
                      case 1:
                          print('you have sleceted balance ')
                          print('yoour balance is 0.00₹')
                      case 2:
                          print('you have sleceted plan ')
                          print('you have no plan')
                      case default:
                          print('you have selected wrong option')
                          
              case 2:
                  print('you have selected postpaid')
                  print('select balance or plan')
                  print('1. balance')
                  print('2. plan')
                  sub1=int(input('select balance or plan: '))
                  match sub1:
                      case 1:
                          print('you have sleceted balance ')
                          print('yoour balance is 0.00₹')
                      case 2:
                          print('you have sleceted plan ')
                          print('you have no plan')
                      case default:
                          print('you have selected wrong option')
              case default:
                print('you have selected wrong option')
    case 3:
           print('you have selected Marathi')
           print('select plan --> prepaid or postpaid')
           print('1. prepaid')
           print('2. postpaid')
           subop=int(input('select plan accordingly: '))
           match subop:
               case 1:
                   print('you have selected prepaid')
                   print('select balance or plan')
                   print('1. balance')
                   print('2. plan')
                   sub1=int(input('select balance or plan: '))
                   match sub1:
                       case 1:
                           print('you have sleceted balance ')
                           print('yoour balance is 0.00₹')
                       case 2:
                           print('you have sleceted plan ')
                           print('you have no plan')
                       case default:
                          print('you have selected wrong option')
               case 2:
                   print('you have selected postpaid')
                   print('select balance or plan')
                   print('1. balance')
                   print('2. plan')
                   sub1=int(input('select balance or plan: '))
                   match sub1:
                       case 1:
                           print('you have sleceted balance ')
                           print('yoour balance is 0.00₹')
                       case 2:
                           print('you have sleceted plan ')
                           print('you have no plan')
                       case default:
                        print('you have selected wrong option')
               case default:
                    print('you have selected wrong option')        
    case default:
        print('you have selected wrong option')

print('*************************************************************************')
#Ask your which operator needs to be perform
# +
# -
# *
# /


print('1. +')
print('2. -')
print('3. *')
print('4. /')

option=int(input('slect from 1-4  following operation: '))
match option:
    case 1:
        print('you have selected + addition')
        num1=float(input('enter the 1st no.: '))
        num2=float(input('enter the 1st no.: '))
        add=num1+num2
        print('addition is: ',add)
    case 2:
        print('you have selected - substraction')
        num1=float(input('enter the 1st no.: '))
        num2=float(input('enter the 1st no.: '))
        sub=num1-num2
        print('substraction is: ',sub)
    case 3:
        print('you have selected * multiplication')
        num1=float(input('enter the 1st no.: '))
        num2=float(input('enter the 1st no.: '))
        mul=num1*num2
        print('multiplication is: ',mul)
    case 4:
        print('you have selected / division')
        num1=float(input('enter the 1st no.: '))
        num2=float(input('enter the 1st no.: '))
        div=num1/num2
        print('division is: ',div)
    case default:
        print('enetred the wrong option')
        


