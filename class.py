class Cat:

    def __init__(self, age, name, parent):
        self.age = age
        self.name = name
        self.parent = parent
    
    def __repr__(self) -> str:
        return f'My name is {self.name} and I am {self.age} years old! I belong to {self.parent}'

Trixie = Cat(3, 'Trixie', 'Ary')
Tofu = Cat(0, 'Tofu', 'Christian')
Merlin = Cat(0, 'Tabi', 'Juan')
Paco = Cat(1, 'Poco Loco', 'James')
Mickey = Cat(5, 'Mickey', 'Jannah')

print(Trixie)
print(Tofu)
print(Merlin)
print(Paco)
print(Mickey)
