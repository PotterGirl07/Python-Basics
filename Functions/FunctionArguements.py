#parameter/arguement(p/a) is a variable for functions
#every time a func is called, some values may change
#that value can be created as a p/a

def addnums(n1,n2):
    total=n1+n2
    print(total)

def subnums(n1,n2):
    total=n1-n2
    print(total)

def mltpynums(n1,n2):
    total=n1*n2
    print(total)

def dvdnums(n1,n2):
    total=n1/n2
    print(total)

addnums(50,60)
addnums(123,456)

subnums(200,100)
subnums(90,33)


#default arguement
#when you call a function and it has no arguement
#then it shouldn't crashout

def greet(name="user"):
    print(f"Hello {name}!")

greet()
greet("Aashra")


mltpynums(7,8)
mltpynums(9,3)

dvdnums(81,9)
dvdnums(121,11)
