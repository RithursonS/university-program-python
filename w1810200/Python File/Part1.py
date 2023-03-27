#Intializing variables
Pass=0
Defer=0
Fail=0

print("----------------------------------------------------")

Pass = int(input("Please enter your credits at pass   : ")) #getting an input
Defer = int(input("Please enter your credits at Defer  : "))#getting an input
Fail = int(input("Please enter your credits at Fail   : "))#getting an input

print("----------------------------------------------------")
#checking the Progression Outcome
if Pass + Defer + Fail == 120:
    if Pass == 120:
        print("Progress")
    elif Pass == 100:
        print("Progress (module trailer)")
    elif Pass == 80 or Pass == 60 or Pass == 40 and Fail < 80:
        print("Do not progress – module retriever")
    elif Pass == 40 and Fail == 80:
        print("Exclude")
    elif Pass == 20 and Fail < 80:
        print("Do not progress – module retriever")
    elif Pass == 20 and Fail == 80 or Fail > 80:
        print("Exclude")
    elif Pass == 0 and Fail < 80:
        print("Do not progress – module retriever")
    elif Pass == 0 and Fail > 80:
        print("Exclude")
else:
    print("Incorrect Total.")

print("----------------------------------------------------")
