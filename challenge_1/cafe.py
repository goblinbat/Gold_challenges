"""
x Create UI:
x     Create menu item
           needs: 
x             id number
x             name
x             description
x             ingredients
x             price
x     view menu items
x     delete menu items

Need:
x     menu class (w/ constructors and instance attributes)
x     menuRepository class (w/ methods)
"""
# About the 3 errors: in MenuRepo, VSC doesn't like that the methods don't have 'self' as an argument, but if I put it in,
# the code doesn't work. So just ignore them, it's fine.


menulist = []

class Menu:
    def __init__(self, idnum, name, desc, ingredients, price):
        self.idnum = idnum
        self.name = name
        self.desc = desc
        self.ingredients = ingredients
        self.price = price
    
    def __repr__(self):
        return self.name


class MenuRepo:
    def add_item(idnum, name, desc, ingredients, price):
        new = Menu(idnum, name, desc, ingredients, price)
        menulist.append(new)
    
    def view_menu():
        return menulist
    
    def delete_menu_item(name):
        for item in menulist:
            if name == item.name:
                index = menulist.index(item)
                del menulist[index]
                return True


while True:
    print('\n')
    print('Welcome to The Komodo Cafe!')
    user_input = input('What would you like to do? (press a number) \n'
                    '1. Add a menu item \n'
                    '2. View menu \n'
                    '3. Delete a menu item \n'
                    '4. Exit \n'
                    '> ')
    print('\n')
    
    if user_input == '1':
        idnum = input("Enter the item's id number: ")
        name = input("Enter the item's name: ")
        desc = input("Enter a brief description of the item: ")
        ingredients = input("Enter a list of the item's ingredients: ")
        price = input("Enter the item's price: ")
        MenuRepo.add_item(idnum, name, desc, ingredients, price)
        print(f'added {name}!')
    elif user_input == '2':
        menu = MenuRepo.view_menu()
        print(menu)
    elif user_input == '3':
        to_del = input('which menu item would you like to delete?: ')
        MenuRepo.delete_menu_item(to_del)
        print(f'{to_del} has been deleted.')
    elif user_input == '4':
        exit(0)
    else: 
        print('invalid input; please enter a number 1-4.')
        pass