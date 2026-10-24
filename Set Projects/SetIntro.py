#set is used to store multiple values together
#they are immutable(changeable)
#they are enclosed in {}

mylist=[1,1,2,2,3,3]
print(mylist)

#set is unique ~ duplicate values will be shown only once
myset={1,1,2,2,3,3}
print(myset)

mylist1=[]
print(type(mylist1))
#alone the curly brackets mean class type dict.
myset1={}
print(type(myset1))
print(type(myset))

#set operations
s1={1,2,3}
s2={3,4,5}
s3={5,6,7}
#union - copmbine all sets with unique values
print(s1.union(s2))
print(s1|s2|s3)
#intersection - show all common values(in no common then it'll show empty set)
print(s1.intersection(s2))
print(s1 & s2)
print(s1 & s2 & s3)
s1={1,2,3,8}
s2={3,4,5,8}
s3={5,6,7,8}
print(s1 & s2 & s3)
#difference - subtracts two sets and shows the remaining value
ns1={3,4,5,6,7}
ns2={1,2,3,4,5}
print(ns1.difference(ns2))
print(ns1-ns2)
