def add(a, b):
    addition= a+b
    return addition
def sub( a, b):
    subraction= a -b;
    return subraction
    
def multi(a ,b):
    multiplication=  a * b;
    return  multipllication
def div( a , b):
    division=  a / b;
    return division;
def mod(a , b):
    modulus= a % b;
    return modulus;
print(" Select Your Operation:");
print("1 Addition")
print("2 Subraction") 
print("3 Multiplication")
print("4 Division")
print("5 Modulus")
while True:
    choice= input("Enter  Your Choice (1/2/3/4/5):")
    if choice in("1","2","3","4","5"):
        a =float(input("Enter the first  Number: "));
        b =float(input("Enter the Second Number:"));
        
        if choice == "1":
            print("The addition of",a ,"and ", b ,"numbers are:" , add(a,b))
        elif choice =="2":
            print("The subraction of",a ,"and ", b ,"numbers are:" , sub(a,b))
        elif choice == "3":
            print("The Multiplication of",a ,"and ", b ,"numbers are:" , multi(a,b))
        elif choice == "4":
            print("The Division  of",a ,"and ", b ,"numbers are:" , div(a,b))
        elif choice == "5":
            print("The Modulus of",a ,"and ", b ,"numbers are:" , mod(a,b))
        else:
            print("Invalid Input")
        break;
    
        
