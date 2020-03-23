import random
User1 = input("Enter name for User1: ")
User1password = input("Enter password for User1: ")
User2 = input("Enter name for User2: ")
User2password = input("Enter password for User2: ")


def login():
    while True:
        username = input('What is your username? ')
        password = input('What is your password? ')
        if username != User1 and username != User2:
            print('Incorrect username, try again')
            continue

        if username == User1:
            while User1password != password:
                print("Incorrect password")
                password = input('What is your password?')
        elif username == User2:
            while User2password != password:
                print("Incorrect password")
                password = input('What is your password?')

        print(f'Welcome, {username} you have successfully logged in.')
        return username


player1 = login()
player2 = login()


def roll(name):
    points = 0

    Roll1 = random.randint(1, 6)
    print(f'{name}, your first roll is {Roll1}')

    Roll2 = random.randint(1, 6)

    print(f'{name}, your second roll is {Roll2}')

    Rollsum = Roll1 + Roll2

    points = points + Rollsum
    if Rollsum % 2 == 0:
        points = points + 2

    if Roll1 == Roll2:
        print("Since you have equal rolls, you get a chance for an extra roll")
        Roll3 = random.randint(1, 6)
        print(f"Your have {Roll3} added to your points")
        points = points + Roll3
    print(f"{name}, your total points are {points}")
    return (points)


Player1Roll = roll(player1)
Player2Roll = roll(player2)


if Player1Roll > Player2Roll:
    print(f"{player1} has won the game!")
elif Player1Roll < Player2Roll:
    print(f"{player2} has won the game!")
else:
    print("Your total points are equal, an extra round will show the winner")
    while Player2Roll == Player1Roll:
        decisive1 = random.randint(1, 6)
        decisive2 = random.randint(1, 6)
        Player1Roll = decisive1
        Player2Roll = decisive2
        if decisive2 < decisive1:
            print(f"{decisive1} has won the game!")
            break
        elif decisive2 > decisive1:
            print(f"{decisive2} has won the game!")
            break