#Intializing variables
x = 0
y = 0
z = 0

print("------------------------------------------------------------")

#Creating a function for Pass
def Pass_fun():
    while True:
        x = input("Please enter your credits at pass   : ")#getting an input
        try:
            x = int(x) #coveting the input into integer
            if x in range(0,121,20):
                break #breaking the loop to stop there
            else:
                print("out of range")
        except:
            print("Integer required")
    return x

#Creating a function for Defer
def Defer_fun():
    while True:
        y = input("Please enter your credits at Defer  : ")
        try:
            y = int(y)
            if y in range(0,121,20):
                break
            else:
                print("out of range")
        except:
            print("Integer required")
    return y

#Creating a function for Fail
def Fail_fun():
    while True:
        z = input("Please enter your credits at Fail   : ")
        try:
            z = int(z)
            if z in range(0,121,20):
                break
            else:
                print("out of range")
        except:
            print("Integer required")
    return z

# calling the function and assingn it 
Pass = Pass_fun()
Defer = Defer_fun()
Fail = Fail_fun()
#calculating the total
total = Pass + Defer + Fail
#checking the Progression Outcome

print("------------------------------------------------------------")

if total == 120:
    try:
        if Pass==120:
            print("Progress")
        elif Pass==100:
            print("Progress (module trailer)")
        elif Pass==80 or Pass==60 or Pass==40 and Fail<80:
            print("Do not progress – module retriever")
        elif Pass==40 and Fail==80:
            print("Exclude")
        elif Pass==20 and Fail<80:
            print("Do not progress – module retriever")
        elif Pass==20 and Fail==80 or Fail>80:
            print("Exclude")
        elif Pass==0 and Fail<80:
            print("Do not progress – module retriever")
        else:
            print("Exclude")
    except:
        "nothing just for eof error"
else:
    print("Incorrect Total")

print("------------------------------------------------------------")

