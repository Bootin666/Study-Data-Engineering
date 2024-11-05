#def Sigma(n):
#   sig=n*(n+1)/2
#    return sig 
#n=int(input('what is n?')) 
#total=Sigma(n) 
#print (total)

#def Sigma1(n):
#    s = sum(range(1, n + 1))
#    return s 
#n=int(input('what is n?')) 
#total=Sigma1(n) 
#print (total)

def Sigma2(n):
    s=0
    for i in range(1, n + 1):
        s += (i)
    return s 
n=int(input('what is n?')) 
total=Sigma2(n) 
print (total)



