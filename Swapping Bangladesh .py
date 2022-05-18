str = 'Bangladesh'
 
a = [a for a in str[0::2] ]
b =  [b for b in str[1::2] ]
 
str2 = ('').join([(i+j) for i,j in zip(b,a)])
 
print(str2)
