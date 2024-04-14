#This function is used to calculate the number of bars the user can buy and the changes.
def Chocolate_bar(total_money,price):
    total_money=int(total_money)
    price=int(price)
    number_bars = total_money // price
    change = total_money % price
    
    return number_bars, change

#example to use
total_money	=100
price = 7
number_bars,change=Chocolate_bar(total_money,price)
print(number_bars,change)