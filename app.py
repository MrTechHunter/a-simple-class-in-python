class AgeCalc:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self):
        return (1400 - self.birth_year)


age_calc1 = AgeCalc("Mahdi", 1378)

print(age_calc1.name)
print(age_calc1.age())
