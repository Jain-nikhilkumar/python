class main:
    def p(self):
        print("Im in parent 1")
class main2:
    def p2(self):
        print("Im in parent  2")
class childh(main,main2):
    def ch(self):
        print("Im in child class")

obj=childh()
obj.ch()
obj.p()
obj.p2()