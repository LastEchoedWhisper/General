supplies = ['scissors','tape','hammer','screws','drill']

for i in range(len(supplies)):
    print ('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print("\n")

for i in range(len(supplies)):
    print ('Item ' + str(i + 1) + ' in supplies is: ' + supplies[i])

print("\n")

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print (spam)

spam1 = ['cat', 'dog', 'bat']
spam1.insert(1, 'chicken')
print (spam1)
