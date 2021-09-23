number1=int(input('ENter number1'))
number2=int(input('ENter number2'))
number3=int(input('ENter number3'))
#sum=number1+number2+number3
def sumofthreenumbers(number1,number2,number3):
    if(number1 == number2 == number3):
        print('Numbers are equal', 3*(number1+number2+number3))
    else: 
        print('Sum of the three numbers are: ',number1+number2+number3)
sumofthreenumbers(number1,number2,number3)
