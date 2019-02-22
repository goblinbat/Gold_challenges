"""
Outing:
    Event Type:
		Golf, Bowling, Amusement Park, Concert
	Number of people that attended,
	Date,
	Total cost per person for the event,
	Total cost for the event

x Make UI
x   Add Outing
x   View all Outings
x   Costs
x       Total cost
x       Cost by type of Outing

Need to do more testing and fix bugs but mostly done I think!
"""

outings = []
totalcost = 0
golfcost = 0
bowlingcost = 0
amusecost = 0
concertcost = 0

class Outing:
    def __init__(self, outtype, attend, date, costper, total):
        self.outtype = outtype
        self.attend = attend
        self.date = date
        self.costper = costper
        self.total = total

    def main_menu():
        print('\nKomodo Outings\n')
        ui = input('What would you like to do?\n'
                    '1) Add Outing\n'
                    '2) View Outings\n'
                    '3) View Costs\n'
                    '4) Exit\n'
                    '> ')
        
        if ui == '1':
            global golfcost
            global bowlingcost
            global amusecost
            global concertcost
            global totalcost
            total = 0

            outtype = input("What type of outing was it (golf, bowling, amusement park, or concert)? ").lower()
            if OutingRepo.valid_outing(outtype): 
                pass
            else:
                print('invalid outing type')
                Outing.main_menu()
            attend = input('How many people went on the outing? ')
            date = input('When was the outing? ')
            costper = input('What was the cost per person? ')
            try:
                total = float(input('What was the total cost of the event? $'))
            except Exception:
                print('invalid cost.')
                Outing.main_menu()
            totalcost += total
            if outtype == 'golf':
                golfcost += total
            elif outtype == 'bowling':
                bowlingcost += total
            elif outtype == 'amusement park':
                amusecost += total
            elif outtype == 'concert':
                concertcost += total
            OutingRepo.add_outing(outtype, attend, date, costper, total)
            print('added outing!')
        elif ui == '2':
            tmp = OutingRepo.get_outings()
            print('Type:\t Attendance: \tDate: \tCost per person: \tTotal Cost: ')
            for outing in tmp:
                print(outing)
        elif ui == '3':
            OutingRepo.view_costs()
            f = input('Press any key to return to main menu \n'
                        ' ')
            if f == True:
                main_menu()
        elif ui == '4':
            exit(0)
        else: 
            print('invalid input, try again')
            pass
        Outing.main_menu()
    
    def __repr__(self):
        return f'{self.outtype}\t{self.attend}\t\t{self.date}\t{self.costper}\t\t\t{self.total}'

class OutingRepo:
    def valid_outing(type_outing):
        valid = ['golf', 'bowling', 'amusement park', 'concert']
        if type_outing in valid:
            return True
        else:
            return False
    
    def add_outing(outtype, attend, date, costper, total):
        outings.append(Outing(outtype, attend, date, costper, total))
        
    
    def get_outings():
        return outings
    
    def view_costs():
        print(f'\nTotal Cost: {totalcost}\n'
                f'Golfing Costs: {golfcost}\n'
                f'Bowling Costs: {bowlingcost}\n'
                f'Amusement Park Costs: {amusecost}\n'
                f'Concert Costs: {concertcost}\n')
        return totalcost



if __name__ == "__main__":
    Outing.main_menu()
