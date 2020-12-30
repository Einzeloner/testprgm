eng = float(input("English marks: "))
maths = float(input("Maths marks: "))
phy = float(input("Physics marks: "))
misc = float(input("Misc marks: "))
chem = float(input("Chemistry marks: "))
total = eng + maths + phy + chem + misc
per = (total / 500) * 100
print("total marks =", total)
print("percentage =", per)
if(per >= 90):
    print("Grade = A")
elif(per >= 80):
    print("Grade = B")
elif(per >= 70):
    print("Grade = C")
elif(per >= 60):
    print("Grade = D")
elif(per >= 40):
    print("Grade = E")
else:
    print("Fail!")

