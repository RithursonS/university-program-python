print("------------------------------------------------------------")
#Intializing variables
x=0
y=0
z=0

a = 0#progress
b = 0#trailer
c = 0#retriever
d = 0#exclude

#Creating a list for Pass, defer, fail
Pass_list = [120,100,100,80,60,40,20,20,20,0]
Defer_list = [0,20,0,20,40,40,40,20,0,0]
Fail_list = [0,0,20,20,20,40,60,80,100,120]


#checking the Progression Outcome
def progression_fun():
    global a,b,c,d

    if total==120:
        try:
            if Pass==120:
                print("Progress")
                a+=1
            elif Pass==100:
                print("Progress (module trailer)")
                b+=1
            elif Pass==80 or Pass==60 or Pass==40 and Fail<80:
                print("Do not progress – module retriever")
                c+=1
            elif Pass==40 and Fail==80:
                print("Exclude")
                d+=0
            elif Pass==20 and Fail<80:
                print("Do not progress – module retriever")
                c+=1
            elif Pass==20 and Fail==80 or Fail>80:
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

    return


for i in range(0,10,1):
    Pass = Pass_list[i]
    Defer = Defer_list[i]
    Fail = Fail_list[i]

    total= Pass + Defer + Fail

    progression_fun()
    

try:
    print()
    print("Horizontal Histogram")
    print("Progress ", a, " :", a * "*")
    print("Trailer  ", b, " :", b * "*")
    print("Retriever", c, " :", c * "*")
    print("Excluded ", d, " :", d * "*")        
except:
    "eof"
print()
print(a+b+c+d,"outcomes in total.")
print("------------------------------------------------------------")
