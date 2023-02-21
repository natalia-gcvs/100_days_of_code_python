def add(*args):
    a = ''
    for n in args:
        a += n
    return a

print(add('n', 'a', 't'))

def calculate(**kwargs):
    print(kwargs)
    for key in kwargs.items():
        print(key)
        print(kwargs)


calculate(add=5, multiply=6)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs.get('model')

my_car = Car(make='Nissan')
print(my_car.model)
