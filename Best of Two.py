# cook your dish here
x=int(input())
for i in range(0,x):
    a,b=map(int,input().split())
    if(a>b):
        print(a)
    else:
        print(b)
