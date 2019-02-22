# testlist = [[1, 2, 'red'], [3, 4, 'blue']]
# a = testlist[0]
# print(a)

# ------------------------------------------------------------------------------------------------------------

claims = []

class Claim:
    def __init__(self, claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid):
        self.claimid = claimid
        self.clmtype = clmtype
        self.desc = desc
        self.amount = amount
        self.incidentdate = incidentdate
        self.claimdate = claimdate
        self.isvalid = isvalid

    def __repr__(self):
        return f"{self.claimid} \t\t{self.clmtype} \t\t{self.desc} \t\t{self.amount} \t\t{self.incidentdate} \t\t{self.claimdate} \t\t{self.isvalid}"

    def make_claim(claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid):
            new = Claim(claimid, clmtype, desc, amount, incidentdate, claimdate, isvalid)
            claims.append(new)

    def display_view_claims():
            print(f"Claim ID: \tClaim Type: \tDescription: \tClaim Amount: \tIncident Date: \tClaim Date: \tClaim Valid:")
            for claim in claims:
                print(claim)

Claim.make_claim(1, 2, 3, 4, 5, 6, 7)
Claim.make_claim('a', 'b', 'c', 'd', 'e', 'f', 'g')
Claim.make_claim(8, 9, 10, 11, 12, 13, 14)
Claim.make_claim('h', 'i', 'j', 'k', 'l', 'm', 'n')

# print(claims)
Claim.display_view_claims()
