#an=2a(n-1)+3
#The first member is 4.
# 2*4+3=11 The second member is 11.
# 2*11+3=25 The third member is 25.
# 2*25+3=53 The forth member is 53.
# 2*53+3=109 The fifth member is 109.
a=4
print("a 1=",a)
#Give the first member.
for i in range(1,5):#Repeat 4 times to calculate the second to fifth values.
    a=2*a+3#Use the equation to calculate.
    print("a",i+1,"=",a)#Print the results.