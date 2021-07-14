#1
'''
n=int(input('n='))
for i in range(1,n+1):
    print(i,'-son: ')
    a = int(input())
    if i==1 :
        katta = a
        kichik = a 
    else:        
        if katta<a: 
            katta = a
        if kichik > a:
            kichik = a        
print('kattasi: ', katta)        
print('kichigi: ', kichik)  
'''
#2
'''
n=int(input('n= '))
for i in range(n):
    a=int(input('a='))
    b=int(input('b='))
    s=a*b
    if i == 0 :
        minum = s
    else:
        if minum > s:
            minum = s
print('kichigi: ', minum)             
'''
#3
'''
n=int(input('n = '))
for i in range(1,n+1):
    a=int(input('a='))
    b=int(input('b='))
    p=2*(a+b)
    if i == 1 :
        maks = p
    else:
        if maks < p:
            maks = p
print('kattasi: ', maks)  
'''
#4      
'''
n=int(input('n='))
for i in range(1,n+1):
    a=int(input('son: '))
    if i == 1:
        mini = a #eng kichigi
        urni = 1 # uning o'rni 
    else:
        if mini > a:
            mini = a
            urni = i
print(urni)
'''
#5
'''
n=int(input('n = '))
for i in range(1,n+1):
    m=int(input('m='))
    v=int(input('v='))
    p=m/v
    if i == 1 :
        maks = p
    else:
        if maks < p:
            maks = p
print('kattasi: ', maks)
'''
#6
'''
n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = N
        min_urni = 1
        mak = N
        mak_urni = 1
    else:
        if min > N:
            min = N
            min_urni = i
        if mak <= N:
            mak = N
            mak_urni = i
print('Eng kichigi o\'rni ' , min_urni)            
print('Eng kattasi o\'rni ', mak_urni)
'''
#7
'''
n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = N
        min_urni = 1
        mak = N
        mak_urni = 1
    else:
        if min >= N:
            min = N
            min_urni = i
        if mak < N:
            mak = N
            mak_urni = i
print('Eng kichigi o\'rni ' , min_urni)            
print('Eng kattasi o\'rni ', mak_urni)
'''
#8
'''
n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = N
        min_urni = 1
        urni = 1
    else:
        if min > N:
            min = N
            min_urni = i
        if min >= N:
            #min = N
            urni = i
print('Birinchi ' , min_urni)            
print('Oxirgisi ', urni)
'''
#9
'''
n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        maks = N
        m_urni = 1
        urni = 1
    else:
        if maks < N:
            maks = N
            m_urni = i
        if maks <= N:
            maks = N
            urni = i
print('Birinchi ' , m_urni)            
print('Oxirgisi ', urni)
'''
#10
'''
n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = mak = N
        min_urni = mak_urni = 1
    else:
        if min > N:
            min = N
            min_urni = i
        if mak < N:
            mak = N
            mak_urni = i
if min_urni < mak_urni :
    print(min_urni)        
else:
    print(mak_urni)    
'''
#11 

n=int(input('Elementlar soni '))
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = mak = N
        min_urni = mak_urni = 1
    else:
        if min >= N:
            min = N
            min_urni = i
        if mak <= N:
            mak = N
            mak_urni = i
if min_urni > mak_urni :
    print(min_urni)        
else:
    print(mak_urni) 

#12 

n=int(input('n='))
kichik = 0
i=0
sanoq=0
while sanoq<n:
    a = int(input())
    if a>0 :
        i+=1

    if i>=1 and a>0 :
        kichik = a
        if kichik > a:
            kichik = a
    sanoq+=1

print(kichik)
