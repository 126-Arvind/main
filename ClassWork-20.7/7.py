# CLASS-OBJECT & CONSTRUCTOR 


# class item:
#     def prip(self,x,y):
#         print("udhay bhardwaj")
#         return x*y
# obj=item()
# obj.name="phone"
# obj.price=1545
# obj.quan=5
# print(obj.prip(obj.price,obj.quan))

# print(type(obj))


#################   constructor     ###########
# class new:
#     def __init__(self,name,price,quan):
#         print("hi i am udhay")
#         self.name=name
#         self.price=price
#         self.quan=quan
#         # print(f"an isntance is created :{name}")
# n=new("phone",100,6)
# k=new("pc",200,6)
# print(n.name)
# print(n.price)
# print(n.quan)
# print(k.name)
# print(k.price)
# print(k.quan)    

 
# ##################### class method ##############
# class person:
#     num_of_people=0
#     def __init__(self,name):
#         self.name=name
#         person.add_people()
    
#     @classmethod
#     def num_of_people_(cls):
#         return cls.num_of_people
#     @classmethod
#     def add_people(cls):
#         cls.num_of_people+=1

# p1=person('udhay')
# p2=person('thomas')
# print(person.num_of_people_())


# #################### static method##########
class math:
    @staticmethod
    def add(x):
        return x+5
print(math.add(5))