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
superHero.print_name()
superHero.health_2()
print(superHero)
print(len(superHero))

