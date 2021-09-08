
with open('names.txt', 'r') as file:
    data = file.read().replace('\n', '').replace('"','')
names = data.split(',')
names.sort()
s= 0
for x in range(len( names)):
    value = 0
    for letter in names[x]:
        value+=(ord(letter)-ord('A')+1)
    value = value*(x+1)
    s+=value
