"""def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello("sahil","poudel",age=24,dob=2000)

lst=list(("sahil", "poudel"))
dict_val ={"age":24,"dob": 2000}

hello(*lst,**dict_val)
def my_function(fname , lname):
  print(fname + lname + " poudel")

my_function("Sahil","prasad")
my_function("Jhalak","prasad")
my_function("Sujan","prasad")
def my_function(*args,**kwargs):
    print(args)
    print(kwargs)
ls=list(("sahil","poudel"))
dc={"age":24,"dob":2000}
my_function(ls,dc)
def sahil1(sahil = "Poudel"):
    print("I live in" + sahil)

sahil1("Jhalak")
sahil1("Sujan")
sahil1()
def nepal(ls):
    for x in ls:
        print(x)

fruits=["mango","apple","banana"]
nepal(fruits)


f1 = 0
f2 = 1
def fibo(x):
    if (x==1 or x ==2):
        return 1
    elif x==0:
        return 0
    else:
        return fibo(x-1) + fibo(x-2)
    
print(fibo(5))
"""

class Car:
    pass

car1=Car()
car2=Car()

car1.windows=4
car1.tires=4
car1.engine="diesel"
car2.windows=6
car2.tires=6
car2.engine="petrol"
print(car1.engine)
print(car2.engine)


