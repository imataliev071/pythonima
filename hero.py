class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def health_2(self):
        self.health_points *= 2

    def __str__(self):
        return f'{self.nickname} \n{self.superpower} \n{self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

    def PrintPeople(self):
        print(self.people)


superHero = SuperHero('zuba', 'Halk', 'speed',
                      50, 'hehe')

class Air(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health_2(self):
        self.health_points **= 2
        self.fly = True
        print(self.health_points)

    def print_t(self):
        print('True in the True_phrase')




class Earth(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = True

    def health_2(self):
        self.health_points **= 2
        self.fly = True
        print(self.health_points)



    def print_t(self):
        print('True in the True_phrase')





class villain(Earth):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2


hero1 = Air('халк', 'стюен', 'сила', 100, 'ааааа', 500)
hero1.print_t()
hero1.health_2()

hero2 = Earth('супермен', 'паркер', 'сила', 100, 'eeeee', 500)
hero2.print_t()
hero2.health_2()

vill = villain('Man', 'men', 'head', 10, 'ooooo', 250)
print(vill.crit())

