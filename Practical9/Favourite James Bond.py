#This function is used to judge favorite James Bond of a person.
def favourite_Bond(born_year):
    born_year = int(born_year)
    start_year=born_year+18
    if start_year>1973 and start_year<1986:
        print("Roger Moore")
    if start_year>1987 and start_year<1994:
        print("Timothy Dalton")
    if start_year>1995 and start_year<2005:
        print("Pierce Brosnan")
    if start_year>2006 and start_year<2021:
        print("Daniel Craig")
    if start_year>2021 or start_year<1973:
        print("There is no data.")
    return born_year

born_year=input("The year in which that person  was born:")

#use the function
favourite_Bond(born_year)
#When you run this file, there will be an input request in the terminal box.
#You can input the born year of the person you want, and then press enter, the result will be there.
#For example: 
#input:2000
#output:Daniel Craig