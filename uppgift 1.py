'''Uppgift 1.
I filen "höjd.txt" finns det två kolumner med värden. Första kolumnen är hur långt längs ett
jogginspår personen kommit. Andra kolumnen är dens höjd. Uppgift 1 går ut på att räkna ut när
längs spåret det lutar mest .'''

distans = []
höjd =[]
with open('höjd.txt') as f:
    rubrik = f.readline()
    for line in f:
        distans.append(int(line.split()[0]))
        höjd.append(int(line.split()[1]))

k=[]

for i in range(1,len(distans)):
    k.append((höjd[i]-höjd[i-1])/(distans[i]-distans[i-1]))

print(k)
max_k=max(k)