# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: …w1810200…………………..…

# Date:  …10/12/2020…………………..…

#Intializing variables
x=0
y=0
z=0
#Intializing variables histogram
a=0#progression
b=0#Trailer
c=0#Retriver
d=0#exclude
#Creating a function for Pass,Defer,Fail
print("------------------------------------------------------------")
def Pass_fun():
    while True:
        x=input("Please enter your credits at pass  : ")#getting an input
        try:
            x=int(x)#(converting the input in to integer)
            if x in range(0,121,20):
                break#breaking the loop to stop there
            else:
                print("out of range")
        except:
            print("Integer required")
    return x
#Creating a function for Defer
def Defer_fun():
    while True:
        y=input("Please enter your credits at Defer : ")
        try:
            y=int(y)
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
        z=input("Please enter your credits at Fail  : ")
        try:
            z=int(z)
            if z in range(0,121,20):
                break
            else:
                print("out of range")
        except:
            print("Integer required")
    return z

def progression_fun():#fuction for progression out come
    global a,b,c,d
    # calling the function and assign it
    Pass = Pass_fun()
    Defer = Defer_fun()
    Fail = Fail_fun()
    #calculating the total
    total = Pass + Defer + Fail
    print("------------------------------------------------------------")
    #checking the Progression Outcome
    if total == 120:
        try:
            if Pass == 120:
                print("Progress")
                a+=1
            elif Pass == 100:
                print("Progress (module trailer)")
                b+=1
            elif Pass == 80 or Pass == 60 or Pass == 40 and Fail<80:
                print("Do not progress – module retriever")
                c+=1
            elif Pass == 40 and Fail == 80:
                print("Exclude")
                d+=1
            elif Pass ==  20 and Fail<80:
                print("Do not progress – module retriever")
                c+=1
            elif Pass == 20 and Fail==80 or Fail>80:
                print("Exclude")
                d+=1
            elif Pass==0 and Fail<80:
                print("Do not progress – module retriever")
                c+=1
            else:
                print("Exclude")
                d+=1
        except:
            "nothing just for eof error"
    else:
        print("Incorrect Total")
    print("------------------------------------------------------------")
    return

progression_fun()

print("Would you like to enter another set of data?")
user_input = input("Enter 'y' for yes or 'q' to quit and view results : ")


while True:
    try:
        if user_input == "y" or user_input== "Y":
            progression_fun()

            #againg asking a user_input
            print("Would you like to enter another set of data?")
            user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
        elif user_input == "q" or user_input== "Q":#if part user_input Q or q program will end printing histogram
            print("------------------------------------------------------------")
            print("Progress ",a," | ","Trailer ",b," | ","Retriever ",c," | ","Excluded ", d)
            try:#https://stackoverflow.com/questions/43563672/python-plotting-a-histogram-downward
                list = [a,b,c,d] 
                rows = 0
                total_number_of_rows = max(list)
                length = 4

                while rows < total_number_of_rows:
                    col = 0
                    while col < length:            
                        if rows < (list[col]):
                            print('    * ', end='         ')
                        else:
                            print('      ', end='         ')
                        col += 1            
                    rows += 1
                    print(" ")
                break
            except:
                print("something wrong")
        else:
            print("Invalid entry")
            print("Would you like to enter another set of data?")
            user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
            
    except:
        print("Invalid entry")
        print("Would you like to enter another set of data?")
        user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
print("------------------------------------------------------------")
    
   
        

