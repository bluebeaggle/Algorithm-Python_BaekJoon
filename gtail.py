a = '10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0 " 200 2222'

import re
print("---------------------1----------------------")
print(a.split("[")[1].split("]")[0])
print()
print("---------------------2----------------------")
print(a.split()[3].strip("[]"))
print()
print("---------------------3----------------------")
print(" ".join(a.split("[" or "]")[3:5]))
print()
print("---------------------4----------------------")
print(" ".join(a.split()[3:]).strip("[]"))
print()
print("---------------------5----------------------")
print(re.split("\[|\]", a)[1])





print("양수만 제곱")
a = [-4,-4,-4,3,3,3,-4,3]
#list = sum(x**2 if x>0 for x in a)
#print(list)
list = sum(x^2 for x in a if x >0)
print(list)
list = sum(x**2 for x in a if x>0)
print(list)
#list = sum(x^2 if x>0 for x in a)
#print(list)


class FunEvent :
    def __init__ (self,tags,year) :
        self.tags = tags
        self.year = year
    
    def __str__(self) :
        return f"FunEvent(tags={self.tags}, year = {self.year})"

tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags,year)
tags.append("bootcamp")
year = 2023

print(bootcamp)



class BaseLayer :
    def __init__(self, name = ""):
        self.name = name
    def __repr__(self):
        return f"{self.name}Layer"

class ActivationLayer(BaseLayer) :
    def __init__(self, size) :
        super().__init__("Activation")
        self.size = size
class FCLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("FulyConected")
        self.size = size
    
print(FCLayer(42))
print(ActivationLayer(51))



