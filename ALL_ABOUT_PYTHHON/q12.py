class sample:
    def __init__(self,n):
        self.no=n
    def __add__(self,obj):
        print("Additon is ",self.no+obj.no)
obj1=sample(20)
obj2=sample(40)
obj1+obj2
