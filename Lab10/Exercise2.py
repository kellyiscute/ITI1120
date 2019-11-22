class Car(object):
    def __init__(self, brand=
    'Ford', color='red', pilot='person', speed=0.):
        self.brand = brand
        self.color = color
        self.pilot = pilot
        self.speed = speed

    def __repr__(self):
        return f'{self.color} {self.brand} driven by {self.pilot}, speed = {self.speed} m/s.'

    def __eq__(self, other: 'Car'):
        return self.brand == other.brand and self.color == other.color and self.pilot == other.pilot and self.speed == other.speed

    def choice_driver(self, name):
        self.pilot = name

    def accelerate(self, flow, duration):
        if self.pilot == 'person':
            print('This car does not have a driver !')
        else:
            self.speed = flow * duration

    def display_all(self):
        print(f'{self.color} {self.brand} driven by {self.pilot}, speed = {self.speed} m/s.')
