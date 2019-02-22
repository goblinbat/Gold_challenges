"""
Broken, not working, making a re-do to implement Connor's suggestion.
See test2.py
"""

from . import badge_repo
import unittest
 

class ChallengeFourTests(unittest.TestCase):

    def test_badge_repo_Badgerepo_create_badge_should_add_badge_to_list(self):
        # Arrange
        self.badgeid = 2
        self.dors = ['3']

        # Act
        badge_repo.BadgeRepo.create_badge(self.badgeid, self.dors)
        actual = len(badge_repo.badges)
        expected = 2

        # Assert
        self.assertEqual(actual, expected)

    def test_badge_repo_badgerepo_view_badges_should_return_list(self):
        # Arrange
        testlist = badge_repo.BadgeRepo.view_badges()

        # Act
        actual = len(testlist)
        expected = 2

        # Assert
        self.assertEqual(actual, expected)

    def test_badge_repo_badgerepo_add_door_should_add_item_to_badge_item_in_list(self):
        # Arrange
        self.bagid = 2
        self.new_door = '6'

        # Act + Assert
        self.assertTrue(badge_repo.BadgeRepo.add_door(self.bagid, self.new_door))
    
    def test_badge_repo_BadgeRepo_delete_door_should_remove_item_from_badge_item_in_list(self):
        # Arrange
        badge_repo.BadgeRepo.create_badge(4, ['6'])
        current = badge_repo.badges[0].doors

        # Act
        badge_repo.BadgeRepo.delete_door(4, '6')
        actual = len(badge_repo.badges[0].doors)
        expected = 0

        # Assert
        self.assertEqual(actual, expected)

    def test_badge_repo_BadgeRepo_delete_badge_should_remove_badge_item_from_list(self):
        # Arrange
        badg = 3
        dor = '3'
        badge_repo.BadgeRepo.create_badge(3, '3')

        # Act + Assert
        self.assertTrue(badge_repo.BadgeRepo.delete_badge(3))
