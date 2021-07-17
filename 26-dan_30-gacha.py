#26
n=int(input('n='))
sanoq=0
for i in range(n):
    N=int(input('N='))
    if N%2==0:
        sanoq+=1
        if sanoq == 1:
            m=sanoq
        if sanoq > m:
            m=sanoq
    else:
        sanoq=0
print(m)

#27
n=int(input('n='))
sanoq=0
m=0
m_urni=0
for i in range(n):
    N=int(input('N='))
    if N == 1:
        sanoq+=1
        if (sanoq == 1)and(sanoq > m):
            m=sanoq
            m_urni=i
        if sanoq > m:
            m=sanoq
            m_urni=i
    else: 
        sanoq=0
print(f'{m} ta bir, {m_urni-sanoq}-o\'rindan boshlangan' )

#28
n=int(input('n='))
sanoq=0
m=0
m_urni=0
for i in range(n):
    N=int(input('N='))
    if N == 1:
        sanoq+=1
        if (sanoq == 1)and(sanoq > m):
            m=sanoq
            m_urni=i
        if sanoq > m:
            m=sanoq
            m_urni=i
    else: 
        sanoq=0
if m !=0 :
    print(f'{m} ta bir, {m_urni-sanoq}-o\'rindan boshlangan' )
else:
    print(0)

#29
n=int(input('n='))
sanoq=0
m=0
for i in range(n):
    N=int(input('N='))
    if i == 0 or N<m:
        m=N
        sanoq=0
        maxnum = 0
    if N==m:
        sanoq+=1
    else:
        if sanoq>maxnum :
            maxnum = sanoq
        sanoq = 0
if (sanoq>maxnum) and (N==m):
    maxnum=sanoq
print(maxnum)
"""
#30
n=int(input('n='))
sanoq=0
m=0
for i in range(n):
    N=int(input('N='))
    if i == 0 or N>m:
        m=N
        sanoq=0
        minnum = n
    if N==m:
        sanoq+=1
    else:
        if sanoq<minnum :
            minnum = sanoq
        sanoq = 0
if (sanoq<minnum) and (N==m):
    minnum=sanoq
print(minnum)

    
    
    
    
