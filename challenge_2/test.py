from .claim import Claim, ClaimRepo, claims
import unittest

class ChallengeTwoTests(unittest.TestCase):

    def test_claim_make_claim_should_add_claim_to_claims_list(self):
        # Arrange
        self.claimid = 2
        self.clmtype = 'theft'
        self.desc = 'my heart'
        self.amount = 10
        self.incidentdate = '2019-02-15'
        self.claimdate = '2019-02-18'
        self.isvalid = 'valid'

        # Act
        ClaimRepo.make_claim(self.claimid, self.clmtype, self.desc, self.amount, self.incidentdate, self.claimdate, self.isvalid)
        actual = len(claims)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)

    def test_claim_view_claims_should_be_equal(self):
        # Arrange

        # Act
        actual = len(claims)
        expected = 1

        # Assert
        self.assertEqual(actual,expected)

    def test_claim_del_claim_should_delete_item_from_list(self):
        # Arrange
        self.claimid = 2
        self.clmtype = 'theft'
        self.desc = 'my heart'
        self.amount = 10
        self.incidentdate = '2019-02-15'
        self.claimdate = '2019-02-18'
        self.isvalid = 'valid'

        # Act + Assert
        ClaimRepo.make_claim(self.claimid, self.clmtype, self.desc, self.amount, self.incidentdate, self.claimdate, self.isvalid)
        self.assertTrue(ClaimRepo.del_claim(self.claimid))


