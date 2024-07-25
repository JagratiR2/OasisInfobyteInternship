import random as ram

symbols = "[]{}()!@#$%^&*"
lower = 'qwertyuioplkjhgfdsazxcvbnm'
upper = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
num = '1234567890'

all = upper+lower+num+symbols
len = 8
password = ''.join(ram.sample(all, len))
print('The password is: ', password)
