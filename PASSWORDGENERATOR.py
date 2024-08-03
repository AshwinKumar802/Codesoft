import random
lower="abdhsbddvhdbdbd"
upper="AHSGSHSBDJDBDHDB"
number="14262673838384748"
all=lower+upper+number
length= int(input ("enter the length of the password "))
T=random.sample(all, length)
password="".join(T)
print(password )