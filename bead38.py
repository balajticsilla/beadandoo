x=input('Adj meg egy számot: ')
y=input('Adj meg egy másik számot: ')
fordx = int(x[::-1])
print(fordx)
fordy = int(y[::-1])
print(fordy)

ossz=fordx+fordy
print(ossz)

ossz=str(ossz)
fordossz=ossz[::-1]
print(fordossz)
print(int(fordossz))
