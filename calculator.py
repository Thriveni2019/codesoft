def add(a,b):
   res=a+b
   return res
def sub(a,b):
   res=a-b
   return res
def mul(a,b):
   res=a*b
   return res
def div(a,b):
   res=a/b
   return res
   
print("\n Select below operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice=input("Enter your choice(1/2/3/4) : ")
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    list1=["1","2","3","4"]
    if choice in list1:
        if choice=="1":
           print("Addition of" ,num1 , "and" , num2 , "=",add(num1,num2))
        elif choice=="2":
           print("Subtraction of" , num1 , "and" , num2 , "=",sub(num1,num2))
        elif choice=="3":
           print("Multiplication of" , num1 , "and" , num2 , "=",mul(num1,num2))
        elif choice=="4":
           print("Division of" , num1 , "and" , num2 , "=",div(num1,num2))
        next=input("Do you want continue(yes/no): ")
        if(next=="no"):
           break
    else:
        print("Entered invalid choice")

