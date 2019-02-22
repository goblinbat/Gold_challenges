
import unittest
from . import green_plan

class ChallengeSixTests(unittest.TestCase):

    def test_green_plan_CarRepo_add_car_should_add_car_to_appropriate_list(self):
        # Arrange
        name = 'Vince Van'
        cartype = 'gas'
        mileage = '3 mpg'
        wheels = 2

        # Act
        green_plan.CarRepo.add_car(name, cartype, mileage, wheels)
        actual = len(green_plan.CarRepo.allcars)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)

    def test_green_plan_CarRepo_show_cars_should_return_list(self):
        # Act
        actual = len(green_plan.CarRepo.show_cars('gas'))
        expected = 1 

        # Assert
        self.assertEqual(actual, expected)

    def test_green_plan_CarRepo_del_car_should_remove_car_from_list(self):
        # Arrange
        delname = 'Terry Truck'
        delcartype = 'electric'
        delmileage = '125 mpg'
        delwheels = 300
        green_plan.CarRepo.add_car(delname, delcartype, delmileage, delwheels)

        # Act + Assert
        self.assertTrue(green_plan.CarRepo.del_car('Terry Truck'))
