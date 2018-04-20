import random
print('Ask a Yes/No question...')
question = input()

messages = ['It is certain', 'It is decidedly so',
            'Definitely', 'Try again', 'Ask later',
            'No', 'My reply is no', 'Outlook is bleak',
            'Very doubtful']

print (messages[random.randint(0, len(messages) - 1)])
