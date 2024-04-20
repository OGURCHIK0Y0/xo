class cat:
    def __init__(self, n, s, b, o):
        self.name= n
        self.size = s
        self.breed= b
        self.outside = o
    def zvuki(self):
        print("meow-meow")
    def eat(self):
        print("fish",'milk','meat' )
    def vneshka(self):
        print('мягкая шерсть',self.size)
    def description(self):
        print('имя ',self.name,' рост ',self.size,' порода',self.breed,'внешка',self.outside)
class dog:
    def __init__(self, n, s, w, c):
        self.nikname = n
        self.size = s
        self.breed = w
        self.outside= c
    def zvuki(self):
        print('woof-woof')
    def eat(self):
        print('bone','pizza','beef')
    def vneshka(self):
        print('более твердая шерсть','рост от 15 до 76')
    def description(self):
        print('имя ' , self.nikname , " рост" , self.size , ' порода' , self.breed,'внешка',self.outside)

pp= dog('Bro','30-40cm','japan','white')
pp.description()
pp2=dog('Jack','15-20cm','germany','brown')
pp2.description()

qq= cat('Bulya','10-20cm','british','black')
qq.description()
qq2= cat('Nick','13-24cm','Sphinx','beige')
qq2.description()
