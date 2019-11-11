c=int(input("enter the percentage"))
if(c<35):
    print("fail")
elif(c>=35) and(c<50):
    print("third class")
elif(c>=50)and(c<60):
    print("second")
elif(c>=60)and(c<85):
    print("first")
elif(c>=85)and(c<100):
    print("disty")
else:
    print(" no mark entered properly")
