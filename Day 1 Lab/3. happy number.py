n=int(input("ENTER ANY NUMBER --> "))
ans=n
l=[]
flag=1
if n>0:
    while ans!=1:
        n=ans
        ans=0
        rem=1
        while n!=0:
            rem=n%10
            n//=10
            ls=[]
            ans+=rem*rem
            ls.append(n)
            ls.append(ans)
            if ls not in l:
                l.append(ls)
            else:
                flag=0
                break
        if flag==0:
            break
        if ans==1:
            print("TRUE")
            break
    if ans!=1:
        print("FALSE")
else:
    print("FALSE")
        
    
