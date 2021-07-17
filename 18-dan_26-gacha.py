#18
n=int(input('n='))
for i in range(1,n+1):
    N=int(input('N='))

    if i == 1:
        maks = N #1-elementni eng katta deb oladi
        tr = i #uning o'rnini saqlaydi 
        tr2=i# eng oxirgisini o'rni
    if maks < N:
    #Eng birinchi maks ni aniqlash u.n        
        maks = N
        tr = i
    if maks == N:
    #eng oxirgi maksni o'rnini aniqlash u.n        
        tr2=i
print(f'eng kattasi {maks}, turgan o`rni {tr}, eng oxirgisi {tr2}')        
if tr!=tr2:
    print(f'ular orasida {tr2-tr-1} ta element bor')                
else:
    print(0)    

#19    
n=int(input('n='))
sanoq=0
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        m=N        
    if m>N:
        m=N
        sanoq = 0
    if m==N:
        sanoq+=1        
print(sanoq)

#20
n=int(input('Elementlar soni '))
sanoq=sanoq1=0
for i in range(1,n+1):
    N=int(input('N='))
    if i == 1:
        min = mak = N
        min_urni = mak_urni = 1
    else:
        if min > N:
            min = N
            min_urni = i
            sanoq1 = 0
        if mak < N:
            mak = N
            mak_urni = i
            sanoq = 0
    if mak==N:
        sanoq+=1 
    if min == N :
        sanoq1+=1
if min_urni < mak_urni :
    print(sanoq)        
else:
    print(sanoq1)   

#Ro'yxatlar yordamida
#20
n=[5,6,9,9,5,6,9]
min_urni = n.index(min(n))
max_urni = n.index(max(n))
print(n.count(max(n)))
print(n.count(min(n)))

#21

n=[5,6,8,7,5,6,9]
n.remove(min(n))
n.remove(max(n))
print(n)
print(sum(n)/len(n))

#22
n=[6,2,3,4,1,6]
b=[]
for i in range(len(n)):
    b.append(min(n))
    del n[n.index(min(n))]
    if len(b)==2:
        break    
print(b)    

#23
n=[1,2,3,4,1,6]
b=[]
for i in range(len(n)):
    b.append(max(n))
    del n[n.index(max(n))]
    if len(b)==3:
        break    
print(b)

#24
n=[1,2,3,5,7,3,1,2,3,6,9,8,7]
b=[]
for i in range(len(n)-1):
    b.append(n[i]+n[i+1])
print(max(b))

#25
n=[1,2,3,5,7,3,1,2,3,6,9,8,11]
b=[]
for i in range(len(n)-1):
    b.append(n[i]*n[i+1])
print(b.index(min(b)), b.index(min(b))+1 )
'''
