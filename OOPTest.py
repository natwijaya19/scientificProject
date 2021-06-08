class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligence (Hero):
    pass

lina = Hero('lina', 100)
techies = Hero_intelligence ('techies', 50)

#%%
print(lina.name)
print(techies.name)

#%%
print(help(techies))

#%%
print(techies.__dict__)


