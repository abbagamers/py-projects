import pprint
car = {'name': 'corsa', 'colour': 'red'}
if  'corsa' in car.values():
    print('true')
elif 'corsa' not in car.values():
    print('false')

message = str(input('What text would you like to see the characters for? '))
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
print(count)