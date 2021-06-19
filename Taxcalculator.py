# n = number what is the percentage of number
# i = for the amount of your percentge
i = int(input("enter I value:"))
#n = int(input("Enter N value:"))
def percentage():
    if (i >= 100000) and (i < 300000):
        print(i);
        print("NO Income Tax below 300000:")
    elif (i >= 300000) and (i <= 500000):
        print(i)
        x = (5 * i / 100)
        print("The amount of tax is payable for %s is ="%(i) ,x)
    elif (i >= 500000) and (i <= 1000000):
        x = (10 * i / 100)
        print(i)
        print("The amount of tax is payable for %s is ="%(i) ,x)
    elif  (i > 1000000) :
        x = (20 *  i / 100)
        print(i)
        print("The amount of tax is payable for %s is ="%(i) ,x)
    else:
        print("NO Income Tax below 300000:")
    
percentage()
