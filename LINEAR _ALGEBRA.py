import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
b=m
print("MATRIX IS:",m)
dt=np.linalg.det(m)
print("DETERMINANT OF MATRIX IS:",dt)
print("\n")
i=np.linalg.inv(m)
print("INVERSE OF MATRIX IS:",i)
print("\n")
n=np.linalg.norm(m)
print("NORM OF MATRIX IS:",n)
print("\n")
r=np.linalg.matrix_rank(m)
print("RANK OF MATRIX IS:",r)
print("\n")
tr=np.trace(m)
print("TRACE OF MATRIX IS:",tr)
p=input("ENTER POWER OF MATRIX:")
power=np.linalg.matrix_power(m,p)
print("POWER OF MATRIX IS:",power)
t=np.transpose(m)
print("TRANSPOSE OF MATRIX IS:",t)
eig=np.linalg.eigvals(m)
print("EIGEN VALUES OF MATRIX IS:",eig)
print("\n")
mx=np.max(a)
print("MAXIMUM OF MATRIX IS:\n",mx)
print("\n")
mi=np.min(a)
print("MINIMUM OF MATRIX IS:",mi)
print("\n")
addi=np.add(a,b)
print("ADDITION OF MATRICES IS:",addi)
subt=np.subtract(a,b)
print("SUBTRACTION OF MATRICES IS:",subt)
mul=np.multiply(a,b)
print("MULTIPLICATION OF MATRICES IS :",mul)
div=np.divide(a,b)
print("DIVISION OF MATRICES IS:",div)



