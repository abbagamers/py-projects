f1 = ['ver', 'lat', 'ham', 'oco']
search = input('Who would you like to search for?')
search = search.lower()
count = 0
for word in f1:
    count += 1
    if word == search:
        print(f"The word is number {count} in F1")
print(search)
#f1.insert(1, 'alo')
print(f1)
f1.sort()

print(f1)

