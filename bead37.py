li=[7, 10, 0, 9, 11, 0, 17]

rend_li=sorted(li)
print(rend_li)
ossz=0
for i in range(len(li)):
    ossz=ossz+li[i]
atlag=ossz/len(li)
print(atlag)


uj_li=[]
for j in range(len(rend_li)):
    if rend_li[j]<atlag:
        pass
    else:
        uj_li.append(rend_li[j])

print(uj_li)

db=0
for k in range(len(li)):
    if li[k]==0:
        db=db+1
print(db)

for l in range(db):
    uj_li.append(0)
print(uj_li)