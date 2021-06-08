#%%
class Animal:
    def eat(self):
        print("I can eat")


class Dog(Animal):
    def bark(self):
        print("I can bark")

class Cat(Animal):
    def get_grumpy(self):
        print("I am getting grumpy")

#%%
dog1 = Dog()
dog1.eat()
dog1.bark()

cat1 = Cat()
cat1.eat()
cat1.get_grumpy()