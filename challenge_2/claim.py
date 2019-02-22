"""
x Make UI
x     Make new claim
x     See claims
x     Take care of claims (Delete a claim)

x Claim class (w/ constructors, class instances, necessary fields)
x ClaimRepo class (w/ methods)
"""
import datetime

claims = []
x = 0
month = datetime.timedelta(days=30)

class Claim:
    def __init__(self, claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid):
        self.claimid = claimid
        self.clmtype = clmtype
        self.desc = desc
        self.amount = amount
        self.incidentdate = incidentdate
        self.claimdate = claimdate
        self.isvalid = isvalid

    def incidentdat():
        incidentdate1 = int(input('Day of the incident (dd): '))
        incidentdate2 = int(input('Month of the incident (mm): '))
        incidentdate3 = int(input('Year of the incident (yyyy): '))
        incidentdate =  datetime.datetime(year = incidentdate3, month = incidentdate2, day = incidentdate1)
        return incidentdate

    def claimdat():
        claimdate1 = int(input('Day the claim was filed (dd): '))
        claimdate2 = int(input('Month the claim was filed (mm): '))
        claimdate3 = int(input('Year the claim was filed (yyyy): '))
        claimdate = datetime.datetime(year = claimdate3, month = claimdate2, day = claimdate1)
        return claimdate

    def display_view_claims():
            for claim in claims:
                print(claim)

    def __repr__(self):
        return f"{self.claimid} \t\t{self.clmtype} \t\t{self.desc} \t{self.amount} \t\t{self.incidentdate} \t{self.claimdate} \t{self.isvalid}"


class ClaimRepo:
    def make_claim(claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid):
        new = Claim(claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid)
        claims.append(new)
    
    def view_claims():
        print(f"Claim ID: \tClaim Type: \tDescription: \tClaim Amount: \tIncident Date:    \tClaim Date: \t\tClaim Valid:")
        for claim in claims:
            print(claim)

    def del_claim(claimid):
        for claim in claims:
            if claimid == claim.claimid:
                index = claims.index(claim)
                del claims[index]
                return True


while x == 0:
    print('\n')
    user_input =input('Komodo Claims Department \n \n'
                    'What would you like to do? \n'
                    '1) Make a new claim \n'
                    '2) View claims \n'
                    '3) Take care of a claim \n'
                    '4) Exit \n'
                    '> ')
    print('\n')
    if user_input == '1':
        claimid = input('Claim id: ')
        clmtype = input('Type of claim (Car, Home, or Theft): ')
        desc = input('Enter a brief description of the incident: ')
        amount = input('How much is the claim for?: ')
        incidentdate = Claim.incidentdat()
        claimdate = Claim.claimdat()
        if claimdate <= (incidentdate + month):
            isvalid = True
        else:
            isvalid = False
        ClaimRepo.make_claim(claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid)
        print('Claim added!')
    elif user_input == '2':
        ClaimRepo.view_claims()
    elif user_input == '3':
        print('Here is the next claim to be handled:\n\n'
            'Claim ID: \tClaim Type: \tDescription: \tClaim Amount: \tIncident Date:    \tClaim Date: \t\tClaim Valid:')
        try:
            tmp = claims[0]
            print(tmp)
            yn = input('Do you want to deal with it now? (y/n) ')
            e = claims[0].claimid
            if yn == 'y':
                ClaimRepo.del_claim(e)
                pass
            elif yn == 'n':
                pass
            else:
                print('invalid input')
                pass
        except Exception: 
            print('no claims available')
            pass
    elif user_input == '4':
        exit(0)
    else:
        print('invalid input')
        pass

    
