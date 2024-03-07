a=40
b=36
c=30
d=(a-b)
e=(b-c)
print("d is",d,"and e is",e)
if d > e:
   print ("d>e The time improvement from running only is greater.")
elif d < e:
   print ("d<e The time improvement from running and strength training is greater.")
else:
   print("d=e These two training regimes are equal.")
#In this case, d is equal to 4, e is equal to 6 and e is greater than d.
#The time improvement from	running	and	strength training is greater.
X=True
Y=False
W=(X or Y) and not (X and Y)
print(W)
#The output is true.
#Thr truth table for W looks like this:
#X     Y     W
#True  True  False
#True  False True
#False True  True
#False False False