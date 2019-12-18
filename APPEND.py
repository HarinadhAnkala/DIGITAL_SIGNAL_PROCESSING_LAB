a=[00,99,88,77,66,55]
b=[1,2,4,5,8,9,0]
f=[00,99,88,77,66,55]
print("\n")
print(a)
print("\n")
print(b)
print("\n")
d=len(b)
for i in range(d):
    a.append(b[i])
print("THE NEW LIST FORMED IS",a)
print("\n")
print("APPENDING USING EVEN CONDITION")
print("\n")
for i in range(len(b)):
    if(b[i]%2==0):
        f.append(b[i])
print("LIST WITH EVEN VALUES APPENDED",f)
print("\n")
