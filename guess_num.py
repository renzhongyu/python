#-*- Coding: UTF-8 -*-

import random

def play_game(num):
    while True:
        a = int(raw_input('Please input a number: '))
        if a > num:
            print('The number is bigger')
        elif a < num:
            print('The number is smaller')
        else:
            print('You are right')
            stop_game()

def stop_game():
    b = str(raw_input('Do you want play again? '))
    if b == 'yes':
        main()
    elif b == 'no':
        print('Game over')
        exit()
    else:
        print("You input error. e.g. 'yes' or 'no'")
        exit()

def main():
    print('--------Begin game-------')
    num = random.randint(0,10)
    play_game(num)

if __name__ == '__main__':
    main()
