"""
x Make UI
x   Add Customer details
x   View Customer details
x   Update Customer details
x   Delete Customer details
x   Exit

x Customer details: first name, last name, type (current, past, potential), email string
x Each customer type has a different email string
"""

import greet

def main_menu():
    print('\nKomodo Insurance\n')
    usin = input('What would you like to do?\n'
                    '1) Add a Customer\n'
                    '2) View Customers\n'
                    '3) Update Customer Details\n'
                    '4) Delete a Customer\n'
                    '5) Exit\n'
                    '> ')
    print('\n')
    if usin == '1':
        firstname = input("customer's first name: ").lower()
        lastname = input("customer's last name: ").lower()
        custype = input("what type of customer are they? (current, past, or potential): ").lower()
        if custype == 'current' or 'past':
            greet.CustomerRepo.add_customer(firstname, lastname, custype)
            print('added customer!')
        elif custype == 'potential':
            greet.CustomerRepo.add_customer(firstname, lastname, custype)
            print('added customer!')
        else:
            print('invalid customer type')
    elif usin == '2':
        print('Name \t\tCustomer type \tEmail')
        a = greet.CustomerRepo.view_customer()
        if len(a) != 0:
            for customer in a:
                print(customer)
        else:
            print('no customers :(')
        back = input('\n\npress any key to return to menu: ')
        if back == True:
            main_menu()
    elif usin == '3':
        fname = input("First name on file of customer to be updated: ").lower()
        lname = input('Last name on file of customer to be updated: ').lower()
        for customer in greet.CustomerRepo.customers:
            if fname == customer.firstname and lname == customer.lastname:
                newfirst = input("Correct first name: ").lower()
                newlast = input("Correct last name: ").lower()
                custype = input("What type of customer are they? (current, past, or potential): ").lower()
                if custype == 'current' or 'past':
                    greet.CustomerRepo.update_customer(fname, lname, newfirst, newlast, custype)
                    print('updated customer!')
                elif custype == 'potential':
                    greet.CustomerRepo.update_customer(fname, lname, newfirst, newlast, custype)
                    print('updated customer!')
                else:
                    print('invalid customer type')
        else:
            print('customer does not exist :(')
    elif usin == '4':
        first = input('First name of customer to be eliminated: ').lower()
        last = input('Last name of customer to be eliminated: ').lower()
        x = greet.CustomerRepo.del_customer(first, last)
        x
        if x == 'frog':
            print('Customer does not exist')
        else:
            print('All gone!')
    elif usin == '5':
        exit(0)
    else:
        print('invalid input')


while True:
    main_menu()
