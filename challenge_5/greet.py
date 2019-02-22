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

class Customer:
    def __init__(self, firstname, lastname, custype, email):
        self.firstname = firstname
        self.lastname = lastname
        self.custype = custype
        self.email = email
    
    def __repr__(self):
        return f'{self.firstname} {self.lastname} \t{self.custype} \t{self.email}'


class CustomerRepo:
    customers = []

    def add_customer(firstname, lastname, custype):
        if custype == 'current':
            email = "Thank you for your loyalty! You will be spared. Here's a coupon."
        elif custype == 'past':
            email = "\tIt's been a while! For your own good, we suggest switching back to us."
        elif custype == 'potential':
            email = "Did you know Komodo Insurance has a wonderful plan for your life? Switch now to find out."
        new = Customer(firstname, lastname, custype, email)
        CustomerRepo.customers.append(new)
    
    def view_customer():
        return CustomerRepo.customers
    
    def del_customer(firstname, lastname):
        for c in CustomerRepo.customers:
            if firstname == c.firstname:
                if lastname == c.lastname:
                    index = CustomerRepo.customers.index(c)
                    del CustomerRepo.customers[index]
                    return True
            else:
                return 'frog'

    def update_customer(firstname, lastname, newfirst, newlast, custype):
            CustomerRepo.del_customer(firstname, lastname)
            CustomerRepo.add_customer(newfirst, newlast, custype)

