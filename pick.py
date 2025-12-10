import random


def pick_ball_experiment():
    ball = ['Blue','Green','Red']
    result= random.choice(ball)

    pro= ball.count('Red')/len(ball)
    print('Probability of Picking Red Ball Is:',pro)

    if result == 'Red':
        return 'Red Ball was picked'
    else:
        return 'Better luck Next Time'



res = pick_ball_experiment()
print(res)