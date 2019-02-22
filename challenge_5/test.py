
import unittest
from . import greet

class ChallengeFiveTests(unittest.TestCase):

    def test_greet_customerrepo_add_customer_should_add_customer_to_list(self):
        # Arrange
        first = 'jon'
        last = 'burger'
        custype = 'past'

        # Act
        greet.CustomerRepo.add_customer(first, last, custype)
        actual = len(greet.CustomerRepo.customers)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)

    def test_greet_customerrepo_view_customer_should_return_list(self):
        # Act
        actual = len(greet.CustomerRepo.view_customer())
        expected = 2

        # Assert
        self.assertEqual(actual, expected)

    def test_greet_customerrepo_del_customer_should_remove_customer_from_list(self):
        # Arrange
        fname = 'sue'
        lname = 'smith'
        custype = 'current'
        greet.CustomerRepo.add_customer(fname, lname, custype)

        # Act + Assert
        self.assertTrue(greet.CustomerRepo.del_customer(fname, lname))



    # I'm not testing update_customer because it's just del_customer and add_customer put into one method
    # which is to say if both of them pass then update should too