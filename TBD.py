from time import gmtime, strftime
import datetime, time

print('Welcome to TBD')
print('Developed by so & so')

print(strftime("%a, %d %b %Y %H:%M:%S %p", gmtime()))
#can replace %Y with any arbitrary number to set a year

what = "What will you do?"

dead = 'You have died, please start over by refreshing the page.'

print('\n')

print(time.ctime())
#more user friendly, like so: Thu Apr 12 13:22:35 2018
