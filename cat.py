import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 50
        self.happiness = 50
        self.health = 100

    def eat(self):
        self.hunger -= 30
        self.health += 5
        print(f"{self.name} поїв.")

    def play(self):
        self.happiness += 20
        self.hunger += 10
        print(f"{self.name} погрався.")

    def sleep(self):
        self.health += 10
        self.hunger += 5
        print(f"{self.name} поспав.")

    def live_one_day(self):
        self.age += 1
        self.hunger += random.randint(5, 15)
        self.happiness -= random.randint(1, 10)

        if self.hunger >= 70:
            self.eat()
        elif self.happiness <= 30:
            self.play()
        else:
            self.sleep()

        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))
        self.health = max(0, min(100, self.health))

        print(
            f"День {self.age}: "
            f"голод = {self.hunger}, "
            f"щастя = {self.happiness}, "
            f"здоров'я = {self.health}"
        )


cat = Cat("Барсик")

for day in range(365):
    cat.live_one_day()

print(f"\n{cat.name} прожив цілий рік!")
