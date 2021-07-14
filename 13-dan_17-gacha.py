#13
'''
n=int(input('Elementlar soni '))
sanoq=0
m_urni = 0

for i in range(1,n+1):
    N=int(input('N='))
    
    if N % 2 == 1: 
        if sanoq==0:
            sanoq = 1
            maks = N
            m_urni = 1
    
        if maks < N and N % 2==1:
            maks = N
            m_urni = i
if m_urni == 0 :
    print(0)            
else:    
    print('Turgan o\'rni: ' , m_urni)            
'''
#14
'''
b=int(input('B='))
sanoq=0
print('10 ta element kiriting:')
for i in range(1,11):
    a=int(input())
    if a>b:
        if sanoq==0 :
            sanoq=1
            m = a #b dan katta son (maks)
            tr = i # uning o'rni (tartib raqami)
        if b<a<m:
            m=a
            tr = i
print('{} dan katta eng kichik son {}'.format(b,m)) 
print("turgan o'rni ", tr)           
'''
#15
'''
b=int(input('B='))
c=int(input('C='))
sanoq=0
print('10 ta element kiriting:')
tr=0
for i in range(1,11):
    a=int(input())
    if b<=i<=c:
        if i==b :
            m = a
            tr = i
        elif m<a :
            m = a
            tr = i         
print('Berilgan oraliqdagi eng katta son: ',m)
print("turgan o'rni ", tr)         
'''
#16
'''
n=int(input('N='))
for i in range(1,n+1):
    a=int(input())
    if i == 1:
        m=a
        tr=1
    elif m>a:
        m=a
        tr=i            
print('Eng kichik elementgacha bo\'lgan elementlar soni: ',tr-1)
'''
#17
n=int(input('N='))
for i in range(1,n+1):
    a=int(input())
    if i == 1:
        m=a
        tr=1
    elif m<=a:
        m=a
        tr=i            
print('Eng katta elementgacha bo\'lgan elementlar soni: ',tr-1)
