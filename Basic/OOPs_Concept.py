class function:
    num=100  # class variable


    def __init__(self, a, b):
        print("When obj created 1st executed")
        self.firstnumber = a
        self.secondnumber = b
        print("Called automatically when i am creating an object")
        

    def greet(self):
        print("I am execute the class")




    def Summation(self):
        return self.firstnumber + self.secondnumber


obj = function(2,4)

obj.greet()
print(obj.num)
print(obj.Summation())