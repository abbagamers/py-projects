import random
#TODO: ability to simulate more teams and scoreboard
morocco = 'morocco'
algeria = 'algeria'
england = 'england'
portugal = 'portugal'
g1 = morocco, algeria
g2 = england, portugal
print(g1[0:2])
print(g2[0:2])
if random.randint(0,1) == 1:
    print('From group 1, morocco wins!')
    g1_win = morocco
else:
    print('From group 1, algeria wins!')
    g1_win = algeria
if random.randint(0,1) == 1:
    print('From group 2, england wins!')
    g2_win = england
else:
    print('From group 2, portugal wins!')
    g2_win = portugal
final = g1_win + g2_win
if random.randint(0,1) == 1:
    print(f'{g1_win} are the winners!')
else:
    print(f'{g2_win} are the winners!')
