#The initial cell culture is at 5% density.
c=5
#The experiment begins at day 1.
d=1
#When the density is less than or equal to 90%, calculates the	density	of	cells	on	each	day.
while c <= 90:
    print("Day",d,"the cell culture is at",c,"percent density.")
    c=2*c
    d=d+1
    #When the density is greater than 90%, stops.
    if c > 90:
        print("There are",d-1,"days before the cell density crosses 90%. (The density goes over 90% at day",d,")")
        print("Taking the reality into account, I must be back at day",d-1,"and have a holiday for",d-2,"days.")
        break
#There are 5 days before the cell density crosses 90%. (The density goes over 90% at day 6 )
#Taking the reality into account, I must be back at day 5 and have a holiday for 4 days.