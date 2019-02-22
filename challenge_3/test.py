import unittest
from . import outing
import pytest

class ChallengeThreeTests(unittest.TestCase):

    def test_outing_add_outing_should_add_outing_to_outings_list(self):
        # Arrange
        self.outtype = 'golf'
        self.attend = 36
        self.date = 'Feb 18'
        self.costper = 45
        self.total = 3500

        # Act
        outing.OutingRepo.add_outing(self.outtype, self.attend, self.date, self.costper, self.total)
        actual = len(outing.outings)
        expected = 1

        # Assert
        self.assertEqual(actual,expected)

    def test_outing_get_outings_should_return_outings_list(self):
        # Arrange
        our_list = outing.OutingRepo.get_outings()

        # Act
        actual = len(our_list)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)
        
    def test_outing_view_costs_should_return_totalcost_variable(self):
        # Arrange
        outing.totalcost = 3500

        # Act
        actual = outing.OutingRepo.view_costs()
        expected = 3500    

        # Assert
        self.assertEqual(actual, expected)
