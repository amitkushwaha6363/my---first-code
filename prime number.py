#prime number between 10 to 50
lower=10
upper=50
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)