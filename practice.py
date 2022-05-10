answer = int(input('player 1 : please insert the number (1,100): '))
is_correct = False
try_count = 0
while try_count < 10 and is_correct == False:
    guess = int(input('player 2 : please guess the number! '))
    if guess == answer:
        print('player 2 wins')
        is_correct = True
    elif guess > answer:
        print('tour guess is greater then the answer.')
        try_count += 1
    else:
        print('tour guess is smaller then the answer.')
        try_count += 1
if is_correct == False:
    print('player 1 wins')