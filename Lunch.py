for i in range(1, 10):
    print('Where we going for lunch?')
    answer = input().lower()
    if answer != 'the habit':
        print('Choose again.')
    else:
        print('Alright, sounds good.')
        break
