while True:
    tesztesetek=int(input("tesztesetek szama: "))
    if 1<=tesztesetek<=100:
        break
sorrend={"+":1,"-":1,"*":2,"/":2,"^":2}
while tesztesetek!=0:
    while True:
        muvelet=input("kifejezés: ")
        if len(muvelet)<=400:
            break
    uj=""
    lst=[]
    tesztesetek=tesztesetek-1
    for ch in muvelet:
        if ch.isalpha():
            uj=uj+ch
        else:
            if ch=="(":
                lst.append(ch)
            elif ch==")":
                operator=lst.pop()
                while operator!="(":
                    uj=uj+operator
                    operator=lst.pop()
            else:
                while len(lst)!=0 and lst[-1]!="(" and sorrend.get(ch)<=sorrend.get(lst[-1]):
                    uj=uj+lst.pop()
                lst.append(ch)
    print(uj)