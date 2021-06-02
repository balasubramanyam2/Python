#Display range of numbers between 1 and 50. classify the output which devide by 3 and 5

n=range(1,51)
for i in n:
    if i%3 ==0 and i%5==0:
        print(i, "with both 3 and 5")
    elif i%3==0 and i%5!=0:
        print(i, "only with 3")
    elif i%3!=0 and i%5==0:
        print (i, "only with 5")
    else:
        print(i, "neither 3 nor 5")
        
