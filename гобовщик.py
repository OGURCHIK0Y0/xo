class NPC:
    def __init__(self, n, s, h, w, p):
        self.name = n
        self.size = s
        self.hp = h
        self.work = w
        self.product =p                  

    def privetstvije(self):
        print("Здравствуйте, меня зовут",self.name,', мой рост',self.size,'сантиметра')
        print(',мое здоровье',self.hp,',моя работа',self.work)
    def proshyaniya(self):
        print('Досвидания от', self.name)
    def servis(self):
        print('купите у меня',self.product)
    
q=NPC('Анатолий','183','Сибирское','таксист','услугу личного таксиста')
q.privetstvije()
q.servis()
q.proshyaniya()

q1=NPC('Валентина','164','Сибирское','доярка','молока по братски!')
q1.privetstvije()
q1.servis()
q1.proshyaniya()

q1=NPC('Акакий','172','Азейборжанское','гробовщик','гроб')
q1.privetstvije()
q1.servis()
q1.proshyaniya()
