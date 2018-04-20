import random
question = input('Ask anything...')
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'No'
    elif answerNumber == 6:
        return 'Ask again later'
    elif answerNumber == 7:
        return 'Maybe'
    elif answerNumber == 8:
        return 'Perhaps'
    elif answerNumber == 9:
        return 'Sure, why not?'

r = random.randint(1,9)
fortune = getAnswer(r)
print (fortune)
