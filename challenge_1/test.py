
import pytest
import unittest
import cafe


class ChallengeOneTests(unittest.TestCase):

    def test_cafe_add_item_should_add_item_to_menulist(self):
        # Arrange
        self.idnum = 6
        self.name = 'burger'
        self.desc = 'ham burger'
        self.ingredients = 'food'
        self.price = 5.99

        # Act
        cafe.MenuRepo.add_item(self.idnum, self.name, self.desc, self.ingredients, self.price)
        actual = len(cafe.menulist)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)

    def test_cafe_view_menu_should_return_menulist(self):
        # Arrange
        # Act
        actual = len(cafe.MenuRepo.view_menu())
        expected = 1

        # Assert
        self.assertEqual(actual,expected)


    def test_delete_menu_item_should_remove_item_from_menulist(self):
        # Arrange
        self.idnum = 6
        self.name = 'burger'
        self.desc = 'ham burger'
        self.ingredients = 'food'
        self.price = 5.99

        # Act
        cafe.MenuRepo.add_item(self.idnum, self.name, self.desc, self.ingredients, self.price)
        self.assertTrue(cafe.MenuRepo.delete_menu_item(self.name))

# Note: comment out cafe.py's run code before testing this becuase it'll run instead