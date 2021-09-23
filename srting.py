String ="Twinkle, twinkle, little star, \n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are"
#print (String)
import datetime
from datetime import date
number= int(input('Enter the numkber: '))
def returnfn(number):
    if(number <100):
        print('less than 100')
    elif (number < 1000 and number >100):
        print('with in 1000 and more than 100')
    elif (number < 2000 and number > 1000):
        print('with in 2000 and more than 1000')

    else:
        print('more than 2000')
returnfn(number)
