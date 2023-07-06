class Customer:
    def __init__(self, first_name, family_name, age):
        self.firts_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.firts_name} {self.family_name}"
    
    def entry_fee(self):
        if self.is_child():
            return 1000
        
        if self.in_adolt():
            return 1500
        
        if self.is_senior():
            return 1200
        
    def is_child(self):
        return 0 <= self.age <= 20
    
    def in_adolt(self):
        return 20 <= self.age <= 65
    
    def is_senior(self):
        return 65 <= self.age

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.full_name())
print(tom.age)
print(tom.entry_fee())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokunaga", age=73)
print(tom.full_name())
print(tom.age)
print(tom.entry_fee())
