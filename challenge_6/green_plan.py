"""
_ UI
_   create ('collect data')
_   list
_       gas list
_       electric list
_       hybrid list
_   delete
_   update  

x 3 lists (gas, electric, hybrid)

"""

class Car:
    def __init__(self, name, cartype, mileage, wheels):
        self.name = name
        self.cartype = cartype
        self.mileage = mileage
        self.wheels = wheels


class CarRepo(Car):
    gaslist = []
    eleclist = []
    hybridlist = []
    allcars = []
    def add_car(name, cartype, mileage, wheels):
        new = Car(name, cartype, mileage, wheels)
        if cartype == 'gas':
            CarRepo.gaslist.append(new)
            CarRepo.allcars.append(new)
        elif cartype == 'electric':
            CarRepo.eleclist.append(new)
            CarRepo.allcars.append(new)
        elif cartype == 'hybrid':
            CarRepo.hybridlist.append(new)
            CarRepo.allcars.append(new)

    def show_cars(cartype):
        if cartype == 'gas':
            return CarRepo.gaslist
        elif cartype == 'electric':
            return CarRepo.eleclist
        elif cartype == 'hybrid':
            return CarRepo.hybridlist
    
    def del_car(name):
        for car in CarRepo.allcars:
            if name == car.name:
                if car.cartype == 'gas':
                    index = CarRepo.gaslist.index(car)
                    del CarRepo.gaslist[index]
                    return True
                elif car.cartype == 'electric':
                    index = CarRepo.eleclist.index(car)
                    del CarRepo.eleclist[index]
                    return True
                elif car.cartype == 'hybrid':
                    index = CarRepo.hybridlist.index(car)
                    del CarRepo.hybridlist[index]
                    return True

    def update_car(name, newname, cartype, mileage, wheels):
        CarRepo.del_car(name)
        CarRepo.add_car(newname, cartype, mileage, wheels)
    
    
    