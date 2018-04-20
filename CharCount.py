message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) #looks for instances of char and returns 0 if it does not find it
    count[character] = count[character] + 1


print (count)
