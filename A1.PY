class class1:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            print("object1 is less than other object")
        else:
            print("object1 is greater than other object")
    
    def __eq__(self,other):
        if(self.a==other.a):
            print("object1 is equal to other object")
        else:
            print("object1 is not equal than other object")

obj1=class1(10)
obj2=class1(20)
print("passed values:",obj1.a,obj2.a)
print(obj1<obj2)


obj1=class1(20)
obj2=class1(20)
print("passed values:",obj1.a,obj2.a)
print(obj1==obj2)