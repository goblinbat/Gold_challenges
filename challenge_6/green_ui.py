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
import green_plan

def main_menu():
    print('\n\nKomodo Insurance\n')
    usin = input('What would you like to do?\n'
                    '1) Collect Car Data\n'
                    '2) View Lists of Cars\n'
                    '3) Delete Car Data\n'
                    '4) Update Car Data\n'
                    '5) Exit\n'
                    '> ')
    print('\n')
    if usin == '1':
        name = input('Name of car: ').lower()
        cartype = input('What type of car is it (gas, electric, or hybrid): ').lower()
        if cartype == 'gas' or 'electric':
            pass
        elif cartype == 'hybrid':
            pass
        else:
            print('invalid car type')
            main_menu()
        mileage = input("What's the car's gas mileage?: ")
        wheels = input('How many wheels does the car have?: ')
        green_plan.CarRepo.add_car(name, cartype, mileage, wheels)
        print('Added car!') 
    elif usin == '2':
        view_menu()
    elif usin == '3':
        name = input("Which car do you want to delete data on? (input it's name): ").lower()
        d = green_plan.CarRepo.del_car(name)
        d
        if d == True:
            print('Deleted car!')
        else:
            print('Car does not exist')
    elif usin == '4':
        name = input('name of car to be updated: ').lower()
        for car in green_plan.CarRepo.allcars:
            if name == car.name:
                newname = input('correct name of car: ').lower()
                cartype = input('What type of car is it (gas, electric, or hybrid): ').lower()
                if cartype == 'gas' or 'electric':
                    pass
                elif cartype == 'hybrid':
                    pass
                else:
                    print('invalid car type')
                    main_menu()
                mileage = input("What's the car's gas mileage?: ")
                wheels = input('How many wheels does the car have?: ')
                green_plan.CarRepo.update_car(name, newname, cartype, mileage, wheels)
            else: 
                print('car does not exist')
                main_menu()
    elif usin == '5':
        exit(0)
    else:
        print('invalid input')


def view_menu():
    print('\nKomodo Insurance\n')
    usin = input('Which type of car would you like to view?\n'
                    '1) Gas\n'
                    '2) Electric\n'
                    '3) Hybrid\n'
                    '4) Back'
                    '> ')
    print('\n')
    if usin == '1':
        print('Name \tType \tMileage \tWheels')
        g = green_plan.CarRepo.show_cars('gas')
        if len(g) != 0:
            for car in g:
                print(f'{car.name} \t{car.cartype} \t{car.mileage} \t\t{car.wheels}')
        else:
            print('no cars available')
        back = input('\n\npress any key to return to menu: ')
        if back == True:
            view_menu()
    elif usin == '2':
        print('Name \tType \tMileage \tWheels')
        e = green_plan.CarRepo.show_cars('electric')
        if len(e) != 0:
            for car in e:
                print(f'{car.name} \t{car.cartype} \t{car.mileage} \t\t{car.wheels}')
        else:
            print('no cars available')
        back = input('\n\npress any key to return to menu: ')
        if back == True:
            view_menu()
    elif usin == '3':
        print('Name \tType \tMileage \tWheels')
        h = green_plan.CarRepo.show_cars('hybrid')
        if len(h) != 0:
            for car in h:
                print(f'{car.name} \t{car.cartype} \t{car.mileage} \t\t{car.wheels}')
        else:
            print('no cars available')
        back = input('\n\npress any key to return to menu: ')
        if back == True:
            view_menu()
    elif usin == '4':
        main_menu()
    else: 
        print('invalid input, please try again')
        view_menu()


if __name__ == '__main__':
    while True:
        main_menu()
